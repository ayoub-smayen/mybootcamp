from  . import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),



]