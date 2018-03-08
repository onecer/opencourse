# _*_ coding:utf-8 _*_
# Author: Onecer <LDH@QQ.COM>
# Date: 1/26/18 4:38 PM
from random import randint

from django.core.mail import send_mail

from users.models import VerifyRecord
from opencourse.settings import EMAIL_HOST_USER


def generate_code(code_length):
    source_chars = 'ABCDEFGHIJKLMNOPQRSTUVWxYZabcdefghijklmnopqrstuvwxyz'
    codes = ''
    for i in range(0, code_length):
        codes += source_chars[randint(0, len(source_chars)-1)]
    return codes


def send_register_email(email, send_type='register'):
    verify_record = VerifyRecord()
    verify_record.verify_code = generate_code(18)
    verify_record.email = email
    verify_record.send_type = send_type
    verify_record.save()
    if verify_record:
        if send_type == 'register':
            email_message = 'http://127.0.0.1:8000/active/{code}'.format(code=verify_record.verify_code)
            email_title = u'欢迎注册开源课程网'
            return send_mail(subject=email_title, from_email=EMAIL_HOST_USER, message=email_message,
                             recipient_list=[email])
        if send_type == 'forget':
            email_message = 'http://127.0.0.1:8000/reset/{code}'.format(code=verify_record.verify_code)
            email_title = u'请点击链接重置密码!'
            return send_mail(subject=email_title, from_email=EMAIL_HOST_USER, message=email_message,
                             recipient_list=[email])
