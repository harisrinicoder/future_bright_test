# project-level urls.py (e.g., future_bright/urls.py)

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('contact/', include('contact.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
