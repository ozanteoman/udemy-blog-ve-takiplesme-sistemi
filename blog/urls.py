from django.conf.urls import url
from .views import posts_list, post_update, post_create, post_delete, sanatcilar, post_detail, add_comment, \
    add_or_remove_favorite, post_list_favorite_user

urlpatterns = [
    url(r'^$', posts_list, name='post-list'),
    url(r'^post-create/$', post_create, name='post-create'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$', post_detail, name='post-detail'),
    url(r'^post-update/(?P<slug>[-\w]+)/$', post_update, name='post-update'),
    url(r'^post-delete/(?P<slug>[-\w]+)/$', post_delete, name='post-delete'),
    url(r'^add-comment/(?P<slug>[-\w]+)/$', add_comment, name='add-comment'),
    url(r'^post-favorite-users/(?P<slug>[-\w]+)/$', post_list_favorite_user, name='post-list-favorite-user'),
    url(r'^add-remove-favorite/(?P<slug>[-\w]+)/$', add_or_remove_favorite, name='add-remove-favorite'),
    url(r'^sanatcilar/(?P<sayi>[0-9a-z]+)/', sanatcilar)
]
