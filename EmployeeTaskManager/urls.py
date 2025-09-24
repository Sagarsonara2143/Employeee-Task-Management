from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet, TaskViewSet
from notes.views import NoteViewSet, TagViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter(trailing_slash=False)
router.register(r'/employees', EmployeeViewSet)
router.register(r'/tasks', TaskViewSet)

router.register(r'/notes', NoteViewSet)
router.register(r'/tags', TagViewSet)


urlpatterns = [
        
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    
]
