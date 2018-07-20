from django.conf.urls import url
import views

app_name = "controlpanel"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^view/(?P<ref_id>[-\w]+)/$', views.view, name="view"),
    url(r'^accept/(?P<ref_id>[-\w]+)/$', views.accept, name="accept"),
    url(r'^reject/(?P<ref_id>[-\w]+)/$', views.reject, name="reject"),
    url(r'^download/(?P<ref_id>[-\w]+)/$', views.download, name="download"),
]