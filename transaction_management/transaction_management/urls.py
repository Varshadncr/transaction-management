# project_name/urls.py (main project `urls.py`)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transactions.urls')),  # Include the transaction app's URLs
]
