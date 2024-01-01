from django.urls import path
from webs.views import PageViews

urlpatterns = [
    path(
        r'',
        PageViews.front_page,
        name='front_page'),
    # Other URL patterns for registration, etc.
]
