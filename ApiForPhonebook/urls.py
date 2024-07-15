# myapp/urls.py
from django.urls import re_path
from ApiForPhonebook import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^api/persons$', views.PeopleApi),
    re_path(r'^api/persons/([0-9]+)$', views.PeopleApi),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)