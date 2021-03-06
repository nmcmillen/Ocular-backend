"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework import routers
from ocular import views
from ocular.serializers import *
from rest_framework_simplejwt.views import ( #new
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'postreactions', views.PostReactionViewSet)
router.register(r'postmessages', views.PostMessageViewSet)
router.register(r'followers', views.FollowerViewSet)
router.register(r'photos', views.PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('ocular.urls')),  # in josh's user auth example not sure if needed
    # path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'), #new
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh') #new
    # path('api/', include('authentication.urls'))
    # path('', include('ocular.urls'))
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
