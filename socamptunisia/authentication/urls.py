from bootcampyub.socamptunisia.socamptunisia.authentication import views as bootcamp_auth_views

urlpatterns = [
    #url(r'^$', core_views.home, name='home'),
    url(r'^$', include('core.urls')),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', bootcamp_auth_views.signup, name='signup'),


]