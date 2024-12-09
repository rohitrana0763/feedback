
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('feedback/',views.feedback, name='feedback'),
    path('feedback/thankyou',views.thank_you, name='thank_you'),
]
