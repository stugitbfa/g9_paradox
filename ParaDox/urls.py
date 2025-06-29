"""
URL configuration for ParaDox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static

# # # project/urls.py while making regiter and login
# # from django.urls import path, include

# # urlpatterns = [
# #     ...
# #     path('accounts/', include('your_app_name.urls')),  # Use the correct app name
# # ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('apps.dashboard.urls')), #connected here

#     # path('admin/', admin.site.urls),
#     # path('', include('apps.dashboard.urls'))
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', include('apps.dashboard.urls')),  # 🔗 Connected here
# # ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
