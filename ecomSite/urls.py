"""ecomSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Login_Signup_App import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page, for now this is just for test purpose to check login and logout is working or not
    path('', views.homePageView, name = 'home'),

    # This line contains path for login / signup apps       
    path('user/signup/', views.Signup, name = 'signup'),
    path('user/login', views.loginUser, name = 'login'),    
    path('user/signup/aguayfiuayshflkashf', views.logoutUser, name = 'logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)