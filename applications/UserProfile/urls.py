from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Homepage, name="Homepage"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('About_us/', views.About_us, name="About_us"),
    path('Resume/', views.Resume, name="Resume"),
    path('Porfolio/', views.Porfolio, name="Porfolio"),
    path('Blog/', views.Blog, name="Blog"),
    path('Contact/', views.Contact, name="Contact"),
    path('Userregisterview/',views.Userregisterview,name="Userregisterview"),
    path('userLogout/',views.userLogout,name="userLogout")
]
