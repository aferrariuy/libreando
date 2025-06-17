"""
URL configuration for libreando project.

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # Import serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]

if settings.DEBUG:
    # Serve SvelteKit _app assets directly. This must come BEFORE the SPA catch-all.
    urlpatterns += [
        re_path(r'^_app/(?P<path>.*)$', serve, {
            'document_root': os.path.join(settings.BASE_DIR, 'frontend', 'build', '_app'),
        }),
    ]
    # Serve other static files (like Django admin static files)
    # Note: STATICFILES_DIRS in settings.py handles general static files from 'frontend/build' via STATIC_URL
    # if they are referenced like /static/file.js
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += [
        re_path(r'^favicon\.png$', serve, {
            'document_root': os.path.join(settings.BASE_DIR, 'frontend', 'static'),
            'path': 'favicon.png',
        }),
    ]

    # Handle MEDIA files if configured
    if hasattr(settings, 'MEDIA_URL') and hasattr(settings, 'MEDIA_ROOT') and settings.MEDIA_URL and settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Catch-all for Svelte SPA routing - this MUST BE THE LAST regular pattern
urlpatterns += [
    re_path(r'^(?!(admin|static|_app|api)(/|$))[^\.]*$', TemplateView.as_view(template_name='index.html')),
]
