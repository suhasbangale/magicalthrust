from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('jobupload', views.jobupload, name='jobupload'),
    path('startupupload', views.startupupload, name='startupupload'),

    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('jobs', views.jobs, name='jobs'),
    path('startups', views.startups, name='startups'),
    path('insights', views.insights, name='insights'),
    path('postnewjob', views.postnewjob, name='postnewjob'),
    path('postnewstartup', views.postnewstartup, name='postnewstartup'),
    path('landing', views.landing, name='landing'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('home', views.home, name='home')
]

