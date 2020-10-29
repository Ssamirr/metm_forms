from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView
from Forms.models import Fields, Forms, Value, Option, Emails, Response
from django.contrib import messages
from django.urls import reverse_lazy 
from django.shortcuts import redirect 
from django.conf import settings 
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
import requests
from asgiref.sync import sync_to_async
import json
import asyncio
import time
from threading import Thread


# Create your views here.

class FormsDetailView(TemplateView):
    template_name = 'forms.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        form = Forms.objects.filter(id=context['pk']).first()
        context['forms'] = form
        context['RECAPTCHA_SITE_KEY'] = settings.RECAPTCHA_SITE_KEY
        return context

    async def post(self, request, *args, **kwargs):
        # messages.success(self.request, 'Form is done')
        
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_secret = settings.GOOGLE_RECAPTCHA_SECRET_KEY
        recaptcha_data = {'secret':recaptcha_secret,'response': recaptcha_response}
        recaptcha_server_response = requests.post(url=url,data=recaptcha_data)
        result = json.loads(recaptcha_server_response.text)

        if result['success'] == False:
            messages.error(self.request, 'Invalid Captcha Try Again')
            redirect_url = reverse_lazy('forms:forms_detail',kwargs={'pk':self.get_context_data(*args, **kwargs)['pk']})
            return redirect(redirect_url)
        ''' End reCAPTCHA validation '''
        


        form = Forms.objects.filter(id=self.get_context_data(*args, **kwargs)['pk']).first()
        global field_value_list
        field_value_list = []
        for field in self.request.POST:
            if field == 'csrfmiddlewaretoken' or field == 'g-recaptcha-response' :
                continue
            else :
                main_field = Fields.objects.filter(label=field).first()
                value = Value(field=main_field,value=self.request.POST[field])
                response = Response(form=form, field=main_field, value=self.request.POST[field])
                response.save()
                field_value = {
                    field : self.request.POST[field]
                }
                field_value_list.append(field_value)
                value.save()

        
        # loop = asyncio.new_event_loop()
        # loop.run_until_complete(asyncio.wait([send_emails(field_value_list,self.get_context_data(*args, **kwargs)['pk']),send_emails(field_value_list,self.get_context_data(*args, **kwargs)['pk']),]))

        # ....................using thread for sending emails.................
        # Thread(target = send_emails, args = (field_value_list,self.get_context_data(*args, **kwargs)['pk'])).start()
        Thread(target = send_emails, args = (field_value_list,self.get_context_data(*args, **kwargs)['pk'])).start()
        return redirect('forms:thanks')

# @sync_to_async
def send_emails(values,id):  #async
    print('asassasddddddddd')
    template_name = 'send_forms_information.html'
    time.sleep(5)
    context = {
        'values': values,
    }
    print(context)
    msg = render_to_string(template_name,context)
    subject = 'New Form'
    emails = Emails.objects.filter(form__id=id)
    message = EmailMessage(subject=subject, body=msg, from_email=settings.EMAIL_HOST_USER, to=emails)
    message.content_subtype = 'html' 
    message.send()


class ThanksView(TemplateView):
    template_name = 'thanks.html'