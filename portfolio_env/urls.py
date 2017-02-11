from django.conf.urls import *
from django.conf import settings
from myapp import views
from django.contrib import admin
from django.views.generic.base import RedirectView


from myapp.views import *

urlpatterns = [

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home_page, name='home'),
	url(r'^photos_of_$', views.user_photos, name='flickr_api'),
	url(r'^maze$', views.maze, name='maze'),
	url(r'^stack$', views.stack),
	url(r'^current_exchange_rate', views.current_exchange_rate, name='current_exchange_rate'),
	url(r'^contact', views.contact_view, name='contact'),
	url(r'^get_best_rate', views.get_best_rate, name='get_best_rate'),

]