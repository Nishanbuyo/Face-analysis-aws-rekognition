from django.urls import path
from .views import home, upload_image, analyze
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home),
    path('upload/', upload_image, name="upload"),
    path('analyze/<str:pk>/', analyze, name="analyze")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)