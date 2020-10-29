from django.urls import path
from Forms.views import  FormsDetailView, ThanksView

app_name = 'forms'

urlpatterns = [
    path('<int:pk>/',FormsDetailView.as_view(),name='forms_detail'),
    path('thanks/',ThanksView.as_view(),name='thanks'),
]