from rest_framework import serializers
from PersonalDashboard_api.models import PersonalMemo

class PersonalMemoSerializer(serializers.ModelSerializer):
   class Meta:
       model = PersonalMemo
       fields = ('id', 'title', 'memoDescription', 'lastEditDate')
