from django.conf.urls import url
from .views import UserRegistrationView, UserAuthenticationView, PersonRegistrationView
app_name="app"
urlpatterns=[
    url(r'register/',UserRegistrationView.as_view(),name='register'),
    url(r'login/',UserAuthenticationView.as_view(),name='login'),
    url(r'person/',PersonRegistrationView.as_view(),name='person')
]