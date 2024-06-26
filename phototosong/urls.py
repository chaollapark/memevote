from django.urls import path
from . import views

app_name = 'phototosong'

urlpatterns = [
    path('', views.upload_photo, name='upload_photo'),  # Map the root URL to the upload view
]
