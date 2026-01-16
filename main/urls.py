from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products_app.urls')),
    path('basket/', include('basket.urls')),
    path('captcha/', include('captcha.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



