from django.conf.urls import url
from wiki import views

urlpatterns = [
    url(r'^$', views.wiki, name='wiki'),
    url(r'^歷年專輯介紹/$', views.歷年專輯介紹, name='歷年專輯介紹'),
    url(r'^成員/$', views.成員, name='成員'),
    url(r'^首張同名專輯/$', views.首張同名專輯, name='首張同名專輯'),
    url(r'^U台灣限定普通版/$', views.U台灣限定普通版, name='U台灣限定普通版'), 
    url(r'^sorrysorry/$', views.sorrysorry, name='sorrysorry'),
    url(r'^Bonamana/$', views.Bonamana, name='Bonamana'),
    url(r'^MAMACITA/$', views.MAMACITA, name='MAMACITA'),
]
