from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^search/',views.get_search, name='get_search'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^update/profile/(\d+)$', views.update_profile, name='update-profile')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
