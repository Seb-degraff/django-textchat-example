from django.urls import path, include
from messenger_app import views

urlpatterns = [
    path('', views.main_view),
    path('all-messages', views.get_all_messages),
    path('login', views.login),
    path('logout', views.logout),
]
