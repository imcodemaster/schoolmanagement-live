from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallary/', views.gallary, name='gallary'),
    path('campus/', views.campus, name='campus'),
    path('notice/', views.notice, name='notice'),
    path('pride/', views.pride, name='pride')
]
