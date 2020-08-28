import django.conf.urls
from . import views

urlpartterns = [
    url(r'^$',view.post_list, name='post_list'),
        ]
