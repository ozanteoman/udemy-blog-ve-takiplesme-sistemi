from django.conf.urls import url
from .views import kullanici_takip_et_cikar, fallowed_or_fallowers_list,kullanici_modal_takip_et_cikar

urlpatterns = [
    url(r'^takiplesme-sistemi/$', kullanici_takip_et_cikar, name='kullanici-takip-et-cikar'),
    url(r'^modal-takip-et-cikar/$', kullanici_modal_takip_et_cikar, name='modal-takip-et-cikar'),
    url(r'^fallowed-or-fallowers-list/(?P<fallow_type>[-\w]+)/$', view=fallowed_or_fallowers_list,
        name='fallowed-or-fallowers-list')
]
