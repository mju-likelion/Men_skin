
from django.contrib import admin
from django.urls import path
import cosmetic.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cosmetic.views.home, name="home")
]
