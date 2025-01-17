from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path(route='aboutus/', view=views.about, name='aboutus'),
    # path for contact us view
    path(route='contactus/', view=views.contact, name='contactus'),

    # path for registration
    path('registration/', views.registration_request, name='registration'),
    # path for login
    path('login/', views.login_request, name='login'),
    # path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view
    path(route='reviews', view=views.about, name='reviews'),
    # path for add a review view
    path(route='addreview', view=views.about, name='addreview'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
