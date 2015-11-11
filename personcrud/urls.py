from django.conf.urls import url
from personcrud import views

urlpatterns = [
   url(r'^$', views.home, name='home')
]
