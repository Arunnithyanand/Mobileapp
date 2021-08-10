from django.urls import path
from customer import views

urlpatterns=[
    path('accounts/registration',views.Registrationview.as_view(),name="signup"),
    path('home',views.CustomerHome.as_view(),name="customerhome"),
    path('accounts/signin',views.SignInView.as_view(),name="signin"),
    path('accounts/signout',views.SignOutView.as_view,name="signout")
]