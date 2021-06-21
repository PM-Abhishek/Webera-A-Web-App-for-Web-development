from django.urls import path

from accounts.views import index,learn,read,events,gallery,about,contact
app_name = 'accounts'

urlpatterns = [
    path('home/', index, name='homepage'),
    path('learn/', learn, name='learnpage'),
    path('read/', read, name='readpage'),
    path('events/', events, name='eventpage'),
    path('gallery/', gallery, name='gallerypage'),
    path('about/', about, name='aboutpage'),
    path('contact/', contact, name='contactpage'),
]
