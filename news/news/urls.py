"""news URL Configuration

"""

#Included pathway that connects the newsweb app url to the main framework
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsweb.urls'))
]
