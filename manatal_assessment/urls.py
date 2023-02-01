
from django.contrib import admin
from django.urls import path, include
from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(core_urls)),
    
]

handler404 = "manatal_assessment.views.page_not_found_view"