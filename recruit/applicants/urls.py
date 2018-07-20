from django.conf.urls import url
import views

app_name = "applicants"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^track/$', views.track, name="track"),
]