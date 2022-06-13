from django.urls import path

from accounts import views

urlpatterns = [

    path('', views.register, name='register'),
    path('doctorview_profile/', views.doctorview_profile, name='doctorview_profile'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patientview_profile/', views.patientview_profile, name='patientview_profile'),
    path('category', views.category, name='category'),
    path('create', views.blog, name='create'),

    path('post_view', views.post_view, name='post_view'),
    path('home', views.home, name='home'),
    path('<slug:c_slug>/', views.home, name='blog_cat'),

]
