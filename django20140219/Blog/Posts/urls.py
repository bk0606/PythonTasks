from django.conf.urls import patterns, include, url

urlpatterns = patterns('Posts.views',
    url(r'^$', 'PostsView'),
    url(r'(?P<id>\d)', 'PostView')
)
