from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Include mocktest app URLs
    path('mocktest/', include('mocktest.urls')),

    # Authentication (if using Django's built-in auth views)
    path('accounts/', include('django.contrib.auth.urls')),

    # Home page (redirect to mocktest home)
    path('', include('mocktest.urls')),  # Updated to use include
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
