# accounts/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.about_view, name='about'),  # Home view for the root URL
    path('about/', views.about_view, name='about'),  # Home view added 
    path('thrill/', views.thrill, name='thrill'),
    path('cultural/', views.cultural, name='cultural'),
    path('nature/', views.nature, name='nature'),
    path('romantic/', views.romantic, name='romantic'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('Tindia/', views.Tindia, name='Tindia'),
    path('Tnz/', views.Tnz, name='Tnz'),
    path('Tsa/', views.Tsa, name='Tsa'),
    path('Taus/', views.Taus, name='Taus'),
    path('Tcr/', views.Tcr, name='Tcr'),
    path('Tnepal/', views.Tnepal, name='Tnepal'),
    path('create_itinerary/', views.create_itinerary, name='create_itinerary'),


]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', views.display_vocabulary, name='display_vocabulary'),
#     path('', views.login, name='login'),
#     path('about/', views.about, name='about'),
#     path('index/', views.index, name='index'),
#     path('profie/', views.profie, name='profie'),
#     path('signup/', views.signup, name='signup'),
#     path('test/', views.test, name='test'),
#     path('test1/', views.test1, name='test1'),
#     path('test2/', views.test2, name='test2'),
# ]