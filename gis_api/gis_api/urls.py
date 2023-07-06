"""
URL configuration for gis_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from plots.views import LoginView, LogoutView, MyPlotsView, ManagePlotView


urlpatterns = [
    path('account/admin/', admin.site.urls),
    path('account/login/', LoginView.as_view(),  name='login-user'),
    path('account/logout/', LogoutView.as_view(), name='logout-user'),
    path("plots/", MyPlotsView.as_view(), name='list-add-plots'),
    path('plots/<int:pk>/', ManagePlotView.as_view(), name='get-update-delete-plot'),
]