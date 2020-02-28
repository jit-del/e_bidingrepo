from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app2 import views
from e_biding import settings

urlpatterns = [
    path('admin/', views.adminlogin, name="admin"),
    path('ho_me/', views.homepage, name="ho_me"),
    path('logincheck/', views.logincheck, name="logincheck"),
    path('pending/', views.pending, name="pending"),
    path('approved/', views.approved, name="approved"),
    path('aadminaprove/', views.adminapoved, name="aadminaprove"),
    path('admindeclint/', views.admindeclint, name="admindeclint"),
    path('admin_declint/', views.admin_declint, name="admin_declint"),
    path('aadmina_prove/', views.aadmina_prove, name="aadmina_prove"),
    path('decliend/', views.decliend, name="decliend"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
