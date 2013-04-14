from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'project.views',
    (r'^$', 'index'),
    (r'^init$', 'init'),
)
