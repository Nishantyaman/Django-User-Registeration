from django.urls import path

from .views import (index_view,

                    register_view,
                    login_view,
                    logout_view)

urlpatterns = [
    path('home',index_view,name='home'),

    path('signup/', register_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
