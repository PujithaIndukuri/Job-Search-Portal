from django.conf.urls import url, include
from jobsearchapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'login$', views.Loginview,name="login"), # Notice the URL has been named
    url(r'home$', views.Homeview,name="home"),
    url(r'search$', views.SearchView,name="search"),
    url(r'results$', views.ResultsView,name="results"),
    url(r'^$', views.Loginview,name="login"),
    ]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
