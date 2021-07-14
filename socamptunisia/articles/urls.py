# coding: utf-8

from django.conf.urls import  include, url

from . import views

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^firechat/$', views.firechat, name='firechat'),
    url(r'^addy/$', views.addIndex, name='addy'),
    url(r'^lochatty/$', views.chatty, name='lochatty'),
    url(r'^piano1/$', views.piano1, name='piano1'),
    url(r'^piano2/$', views.piano2, name='piano2'),
    url(r'^rubikGame/$', views.rubikGame, name='rubikGame'),
    url(r'^mainCraft/$', views.mainCraft, name='mainCraft'),
    url(r'^addNotes/$', views.addNotes, name='addNotes'),
     url(r'^savenotes/$', views.savenotes, name='savenotes'),


    url(r'^myeditor/$', views.myeditor, name='myeditor'),
    url(r'^write/$', views.write, name='write'),
    url(r'^preview/$', views.preview, name='preview'),
    url(r'^drafts/$', views.drafts, name='drafts'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^tag/(?P<tag_name>.+)/$', views.tag, name='tag'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit_article'),
    url(r'^(?P<slug>[-\w]+)/$', views.article, name='article'),
]