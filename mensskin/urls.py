
from django.contrib import admin
from django.urls import path
import cosmetic.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cosmetic.views.home, name="home"),
    path('find_foundation/',cosmetic.views.find_foundation, name="find_foundation"),
    path('foundation_result/',cosmetic.views.foundation_result, name="foundation_result"),
]
