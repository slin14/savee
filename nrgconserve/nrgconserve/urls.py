"""nrgconserve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path
from savee.views import fetch_neighbourhood, fetch_rankings, fetch_electricity_use
=======
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

from savee.views import fetch_neighbourhood, fetch_rankings
>>>>>>> 6efd21cb78c17884f5683daadc35c8db85165993

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetch_house/', fetch_neighbourhood),
    path('fetch_rankings/', fetch_rankings),
<<<<<<< HEAD
    path('fetch_electricity_use/', fetch_electricity_use)
]
=======

    path('savee/', include('savee.urls')),
    path('', RedirectView.as_view(url='savee/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 6efd21cb78c17884f5683daadc35c8db85165993
