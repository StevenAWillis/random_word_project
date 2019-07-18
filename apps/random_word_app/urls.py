from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.random_word),
    url(r'^random_word/reset$', views.random_word_reset),
]