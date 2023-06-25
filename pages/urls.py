from django.urls import path
from . import views

urlpatterns = [
    path("aboutus/" , views.aboutus.as_view() , name="aboutus"),
    path("callus/" , views.callus.as_view() , name="callus"),




]