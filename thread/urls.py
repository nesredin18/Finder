from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('thread/',views.getallth),
    path('thread/lost-person', views.getlostp),
    path('thread/lost-item', views.getlosti),
    path('thread/found-person', views.getfoundp),
    path('thread/found-item', views.getfoundi),
    path('thread/lost-person/<str:pk>/', views.getlostpid),
    path('thread/lost-item/<str:pk>/', views.getlostiid),
    path('thread/found-person/<str:pk>/', views.getfoundpid),
    path('thread/found-item/<str:pk>/', views.getfoundiid),
    path('thread/post-lost-person', views.createlostp),
    path('thread/update-lost-person/<str:pk>/', views.updatelostp),
    path('thread/delete-lost-person/<str:pk>/', views.deletelostp),
    path('login/',views.loginAccount),
    path('logout/',views.logoutAccount),
    path('log/',views.getThread),
    path('register/',views.registeruser),
    path('send/',views.send_otp),
    path('verify-email/',views.VerifyEmail,name='emailverify'),
    
]