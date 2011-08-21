from django.conf.urls.defaults import patterns, url

from fragments.views import FragmentCreate, FragmentDetail, FragmentList

urlpatterns = patterns('',
    url(r'^$', FragmentList.as_view(), name="fragments_fragment_list"),
    url(r'^create/', FragmentCreate.as_view(), name="fragments_fragment_create"),
    url(r'^(?P<pk>[0-9]+)/', FragmentDetail.as_view(), name="fragments_fragment_detail"),
)
