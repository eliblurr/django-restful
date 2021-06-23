from django.views.decorators.csrf import csrf_exempt
from django.urls import path, re_path
from .views import SnippetView, index

app_name = 'snippet_api'

r_opt = r'^snippets/(?:/(?P<pk>[0-9]+))?(?:/(?P<search>[a-zA-Z]+))?(?:/(?P<value>[a-zA-Z]+))?(?:/(?P<offset>[0-9]+))?(?:/(?P<limit>[0-9]+))?'
r_opt_pk = r'^snippets/(?P<pk>\w+)'

urlpatterns = [
    path('', index, name='index'),
    re_path(r_opt_pk, SnippetView.as_view(), name='pk_mandatory'),
    re_path(r_opt, SnippetView.as_view(), name='pk_opt_with_search'),
]