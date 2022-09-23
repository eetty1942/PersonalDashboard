from django.urls import include, path
from rest_framework import routers
from PersonalDashboard_api.views import PersonalMemoViewSet

router = routers.DefaultRouter()
router.register(r'PersonalMemo', PersonalMemoViewSet)
# router.register(r'species', SpeciesViewSet)

urlpatterns = [
   path('', include(router.urls)),
]