from rest_framework import fields, serializers
from .models import *
from django.conf import settings


class BlogSerializer(serializers.ModelSerializer):
      class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'timestamp')




class ReportSerializer(serializers.ModelSerializer):
        symptoms = fields.CharField(required=False)
        # filling_for_who = serializers.ChoiceField(choices=FILLING_CHOICES)
        # title = serializers.ChoiceField(choices=TITLE_CHOICES)
        # gender = serializers.ChoiceField(choices=GENDER_CHOICES)
        class Meta:
                model=Report
                managed = True
                verbose_name = 'Report'
                verbose_name_plural = 'Reports'
                fields="__all__"

        

