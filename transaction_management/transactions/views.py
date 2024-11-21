from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Transaction Management API!")

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return self.queryset.filter(user_id=user_id)
        return self.queryset
