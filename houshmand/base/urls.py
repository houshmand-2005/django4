from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('room/<str:pk>/',views.room,name='room'),
    path('profile/<str:pk>',views.userProfile,name='userProfile'),
    path('create-room/',views.createroom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('update-user/',views.updateUser,name='update-user'),
    path('topics/',views.topicsPage,name='topics'),
    path('logoutUserRE/',views.logoutUserRE,name='logoutUserRE'),
    path('activity/',views.activatePage,name='activity'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name='base/password_reset.html'),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='base/reset_password_sent.html'), 
        name="password_reset_done"),

    path('asdni/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html'), 
     name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='base/reset_password_complete.html'), 
        name="password_reset_complete"),




]
