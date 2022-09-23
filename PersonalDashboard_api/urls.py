from django.urls import include, path
from rest_framework import routers
from PersonalDashboard_api.views import PersonalMemoViewSet

router = routers.DefaultRouter()
router.register('PersonalMemo', PersonalMemoViewSet)


urlpatterns = [
   path('', include(router.urls)),
]