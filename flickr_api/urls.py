from django.conf.urls import *
from django.conf import settings
from myapp import views
from django.contrib import admin

from myapp.views import *

urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home_page, name='home'),
	url(r'^photos_of_$', views.user_photos),
	url(r'^maze$', views.maze),
	url(r'^stack$', views.stack),
	url(r'^current_exchange_rate', views.current_exchange_rate),
	url(r'^contact', views.contact_view),


]