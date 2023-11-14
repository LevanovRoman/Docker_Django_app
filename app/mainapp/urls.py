from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import *

urlpatterns = [
    # path('', LoginUser.as_view(), name='login-url'),
    path('oauth2/', include('django_auth_adfs.urls')),
    # path('', login_user, name='login-url'),
    path('', HomeView.as_view(), name='home'),
    path('oauth2/login/', Login_url.as_view(), name='login'),
    path('oauth2/login_no_sso/', Login_no_sso_url.as_view(), name='login_no_sso'),
    path('oauth2/callback/', Callback_url.as_view(), name='callback'),
    path('oauth2/logout/', Logout_url.as_view(), name='logout'),
    path('user_data/', user_data, name='user_data'),
    path('user_mail/', user_mail, name='user_mail'),
    # path('logout/', logout_user, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
