"""django_project_example URL Configuration

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
from django.conf.urls import url
import example_processing_app.views as views
from logger import *
import logging

log_config = Log()
logging.basicConfig(filename=log_config.log_config["filename"],
                    level=log_config.log_config["level"],
                    format=log_config.log_config["format"],
                    datefmt=log_config.log_config["datefmt"])

urlpatterns = [
    url(r'^app_status', views.app_status, name="app_status")
]
