from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('location', 'temperature', 'created_at', 'type')