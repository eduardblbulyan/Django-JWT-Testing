"""
URL configuration for simplejwt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# migrate before doing this
# for test we can use superuser admin(create it via manage.py)(admin,admin,admin@admin.com)
# check in Postman by sendin http://localhost:8000/api/token/ ("POST")
# Body -> x-www-form-urlencoded
# set `username`, `password`

# or curl this
"""
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'password=admin' \
--data-urlencode 'username=admin'
"""