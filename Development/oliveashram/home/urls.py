from unicodedata import name
from django.urls import path
from home import views
urlpatterns =[
    path('',views.index,name="home"),
    path('index',views.index,name="home"),
    path('contact',views.contact,name='contact'),
    path('news',views.news,name="news"),
    path('mission',views.mission,name="mission"),
    path('services',views.services,name="services"),
    path('about/history',views.history,name="history"),
    path('about/charism',views.charism,name="charism"),
    path('about/founder',views.founder,name="founder"),
    path('about/members',views.members,name="members"),
    path('mission/vision',views.vision,name="vision"),




]