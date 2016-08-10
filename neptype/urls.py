from django.conf.urls import url

from . import views, ajax

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^signup/', views.signup, name='signup'),
        url(r'^signin/', views.signin, name='signin'),
        url(r'^verify/', views.emailverify, name='emailverify'),
        url(r'^home/', views.home, name='home'),
        url(r'^logout/', views.signoff, name='signoff'),
        url(r'^race/', views.race, name='race'),
        url(r'^ajax/load_text/$', ajax.load_text, name='load_text'),
        url(r'^ajax/update_speed/$', ajax.update_speed, name='update_speed'),
        ]
