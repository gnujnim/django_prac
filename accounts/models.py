from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from django.template.loader import render_to_string

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', "Female"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    profile_img = models.ImageField(blank=True, upload_to='accounts/profile_img/%Y/%m/%d',
                                    help_text='48px * 48px 크기의 png/jpg 파일을 업로드 해주세요')

    @property 
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property 
    def profile_img_url(self):
        if self.profile_img:
            return self.profile_img.url
        else:
            return resolve_url('pydenticon_image', self.username)

    def send_welcome_email(self):
        pass
        # subject = render_to_string('accounts/welcome_email_subject.txt', {
        #     "user" : self,
        # })
        # content = render_to_string('accounts/welcome_email_content.txt', {
        #     "user" : self,
        # })
        # sender_mail = settings.WELCOME_EMAIL_SENDER
        # send_mail(subject,
        #           content,
        #           sender_mail,
        #           [self.email],
        #           fail_silently=False,)