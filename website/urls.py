from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('record/<int:pk>', views.hoa_oc, name='record'),
    path('delete_record/<int:pk>', views.delete_oc, name='delete_record'),
    path('add_record/', views.add_oc, name='add_record'),
    path('update_record/<int:pk>', views.update_oc, name='update_record'),
]
