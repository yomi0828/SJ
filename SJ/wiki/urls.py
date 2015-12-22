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
    url(r'^LeeTeuk/$', views.LeeTeuk, name='LeeTeuk'),
    url(r'^HeeChul/$', views.HeeChul, name='HeeChul'),
    url(r'^YeSung/$', views.YeSung, name='YeSung'),
    url(r'^KangIn/$', views.KangIn, name='KangIn'),
    url(r'^ShinDong/$', views.ShinDong, name='ShinDong'),
    url(r'^SungMin/$', views.SungMin, name='SungMin'),
    url(r'^EunHyuk/$', views.EunHyuk, name='EunHyuk'),
    url(r'^SiWon/$', views.SiWon, name='SiWon'),
    url(r'^DongHae/$', views.DongHae, name='DongHae'),
    url(r'^RyeoWook/$', views.RyeoWook, name='RyeoWook'),
    url(r'^KyuHyun/$', views.KyuHyun, name='KyuHyun'),
    
    url(r'^category/(?P<categoryID>[\w\-]+)/$', views.category, name='category'),
    url(r'^addCategory/$', views.addCategory, name='addCategory'), 
    url(r'^addPage/(?P<categoryID>[\w\-]+)/$', views.addPage, name='addPage'),
    url(r'^deleteCategory/(?P<categoryID>[0-9]+)/$', views.deleteCategory,name='deleteCategory'),
    url(r'^deletePage/(?P<pageID>[0-9]+)/$', views.deletePage, name='deletePage'),
    url(r'^addCategory/$', views.addCategory, name='addCategory'), 
    url(r'^updateCategory/(?P<categoryID>[0-9]+)/$', views.updateCategory, name='updateCategory'),
    url(r'^updatePage/(?P<pageID>[0-9]+)/$', views.updatePage, name='updatePage'),
]
