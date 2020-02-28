from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app1 import views
from e_biding import settings

urlpatterns = [
    path('',views.user,name="user"),
    path('u_logincheck',views.userlogin,name="u_logincheck"),
    path('register/',views.register,name="register"),
    path('registersucces/',views.registersucces,name="registersucces"),
    path('log_out/',views.log_out,name="log_out"),
    path('home_user/',views.home_user,name="home_user"),
    path('seller/',views.seller,name="seller"),
    path('add_product/',views.productadd,name="add_product"),
    path('product/',views.product,name="product"),
    path('view_product/',views.view_product,name="view_product"),
    path('delete_product/',views.delete_product,name="delete_product"),
    path('not_biding/',views.not_biding,name="not_biding"),
    path('biding/',views.biding,name="biding"),
    path('biding_/',views.biding_,name="biding_"),
    path('buyer/',views.buyer,name="buyer"),
    path('save_bid/',views.save_bid,name="save_bid"),
    path('bid_view/',views.bid_view,name="bid_view"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
