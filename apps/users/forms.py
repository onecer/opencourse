# _*_ coding:utf-8 _*_
# Author: Onecer <LDH@QQ.COM>
# Date: 1/23/18 4:17 AM
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
