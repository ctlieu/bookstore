from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.store, name='store'),
    url(r'^$', views.index, name='index'), 

]
