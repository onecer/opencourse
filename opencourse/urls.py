"""opencourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin

from users.views import LoginView, RegisterView, ActiveView, ForgetPwdView, ResetView


urlpatterns = [
     url(r'^captcha/', include('captcha.urls')),
     url(r'^xadmin/', xadmin.site.urls),
     url(r'^admin/', admin.site.urls),
     url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
     url(r'^login/$', LoginView.as_view(), name='login'),
     url(r'^register/$', RegisterView.as_view(), name='register'),
     url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name='active'),
     url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
     url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
]
