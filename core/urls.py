from rest_framework_nested import routers
from django.urls import path,include
from apis.views import StudentViewSet, SchoolViewSet ,LogEntryViewSet


router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)
router.register(r'logs', LogEntryViewSet)

schools_router = routers.NestedDefaultRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentViewSet, basename='school-students')


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(schools_router.urls)),
]

