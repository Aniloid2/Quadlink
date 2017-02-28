"""QuadLink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url

from django.contrib import admin

from authentication.views import Rlogin

from logout.views import Rlogout

from registeruser.views import registeruser

from registerquad.views import registerquad

from realtimeup.views import realtimeup



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', Rlogin, name="login"),

    url(r'^logout/$', Rlogout, name="logout"),

    url(r'^registeruser/$', registeruser, name="registeruser"),

    url(r'^registerquad/$', registerquad, name="registerquad"),
    
    url(r'^realtimeup/$', realtimeup, name = "realtimeup"),

]
