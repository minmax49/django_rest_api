from rest_framework import serializers 
from worklist.models import CaseDetail, TotalView
 


class CaseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseDetail
        fields = '__all__'

class TotalViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalView
        fields = '__all__'