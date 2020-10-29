# ......sendigm emails with celery...............

# from celery import shared_task
# from Forms.models import Emails
# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage, send_mail
# from django.conf import settings 
# from time import sleep




#     @shared_task
#     def send_emails(values,id):
#     template_name = 'send_forms_information.html'
#     context = {
#         'values': values,
#     }
#     print(context)
#     msg = render_to_string(template_name,context)
#     subject = 'New Form'
#     emails = Emails.objects.filter(form__id=id)
#     message = EmailMessage(subject=subject, body=msg, from_email=settings.EMAIL_HOST_USER, to=emails)
#     message.content_subtype = 'html' 
#     message.send()

# def mails(values,id):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     asyncio.run(send_emails(values,id))
    # loop.run_until_complete(aiosmtplib.send(message))
    # loop.run_until_complete(asyncio.wait([send_emails(values,id)]))
 
    

