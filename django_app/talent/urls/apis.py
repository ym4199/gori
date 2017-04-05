from django.conf.urls import url

from .. import apis

app_name = 'talent'

urlpatterns = [
    url(r'^list/$', apis.TalentList.as_view(), ),
    url(r'^detail-all/(?P<pk>[0-9]+)/$', apis.TalentDetail.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', apis.TalentShortDetail.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/location/$', apis.LocationRetrieve.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/classimage/$', apis.ClassImageRetrieve.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/curriculum/$', apis.CurriculumRetrieve.as_view()),
    url(r'^mywishlist/$', apis.MyWishList.as_view()),
    url(r'^myregislist/$', apis.MyRegistrationList.as_view()),
    url(r'^list/location/$', apis.LocationList.as_view()),
    url(r'^registration/$', apis.RegistrationList.as_view()),
    url(r'^(?P<pk>[0-9]+)/registration/$', apis.TalentRegistration.as_view()),
]
