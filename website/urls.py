from django.urls import include , path
from website.views import *
urlpatterns = [
    path('', base_view)
]
