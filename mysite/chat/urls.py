from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path("send-message/", send_message),
    path("test/", indexs )

]
