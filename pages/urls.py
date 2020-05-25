from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]


"""
path(route, view, kwargs=None, name=None)
In order to perform URL reversing, you’ll need to use named URL patterns as done in the examples above. The string used for the URL name can contain any characters you like. You are not restricted to valid Python names.
When naming URL patterns, choose names that are unlikely to clash with other applications’ choice of names. If you call your URL pattern comment and another application does the same thing, the URL that reverse() finds depends on whichever pattern is last in your project’s urlpatterns list.
"""
