from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'status', 'timestamp', 'user']

    def create(self, validated_data):
        # Set default status and timestamp if not provided
        if 'status' not in validated_data:
            validated_data['status'] = 'PENDING'  # Default status
        if 'timestamp' not in validated_data:
            from django.utils import timezone
            validated_data['timestamp'] = timezone.now()
        
        return super().create(validated_data)
