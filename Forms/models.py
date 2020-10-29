from django.db import models

# Create your models here.

class Forms(models.Model):
    name = models.CharField('Name',max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=False)

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
    
    def __str__(self):
        return self.name

class Fields(models.Model):
    field_type_choice = [
        ('1', 'Text Area'),
        ('2', 'Integer'),
        ('3', 'Date Time'),
        ('4', 'Date'),
        ('5','Text'),
        ('6', 'Selector')
    ]
    validation_type_choice = [
        ('1', 'Email'),
        ('2', 'Text'),
        ('3', 'Integer')
    ]
    form = models.ForeignKey(Forms,on_delete=models.CASCADE, db_index=True, related_name='fields')
    label = models.CharField('Label',max_length=256)
    field_type = models.CharField('Type',max_length=15,choices=field_type_choice)
    default_value = models.CharField('Defaul Value', max_length=1024, null=True, blank=True, default=' ')
    validation = models.CharField('Validation',max_length=15,choices=validation_type_choice)
    requirement = models.BooleanField('Requirement',default=False)
    is_published = models.BooleanField('is published', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Field'
        verbose_name_plural = 'Fields'
    
    def __str__(self):
        return self.label

class Value(models.Model):
    field = models.ForeignKey(Fields,on_delete=models.CASCADE, db_index=True, related_name='field_name')
    value = models.TextField('Value')

    class Meta:
        verbose_name = 'Value'
        verbose_name_plural = 'Values'

    def __str__(self):
        return self.field.label

class Option(models.Model):
    field = models.ForeignKey(Fields,on_delete=models.CASCADE, db_index=True, related_name='field_name_select')
    option = models.CharField('Option',max_length=20)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.field.label

class Emails(models.Model):
    form = models.ForeignKey(Forms,on_delete=models.CASCADE, db_index=True, related_name='forms_sends_to')
    email = models.CharField('Emails',max_length=64)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email

class Response(models.Model):
    form = models.ForeignKey(Forms,on_delete=models.CASCADE, related_name='responses_form')
    field=models.CharField('Question',max_length=1001,)
    value = models.TextField('Answer')

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'

    def __str__(self):
        return self.form.name


# class ResponseQA(models.Model):
#     response = models.ForeignKey(Response,on_delete=models.CASCADE, related_name='answers_response')


#     class Meta:
#         verbose_name = 'ResponseQA'
#         verbose_name_plural = 'ResponseQAs'

#     def __str__(self):
#         return self.response.form.name




    