
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import cosmetic.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cosmetic.views.home, name="home"),
    path('find_foundation/',cosmetic.views.find_foundation, name="find_foundation"),
    path('foundation_result/',cosmetic.views.foundation_result, name="foundation_result"),
    path('mens_ranking/',cosmetic.views.mens_ranking, name="mens_ranking"),
    path('mens_rankingdetail1/',cosmetic.views.mens_rankingdetail1, name="mens_rankingdetail1"),
    path('mens_rankingdetail2/',cosmetic.views.mens_rankingdetail2, name="mens_rankingdetail2"),
    path('search_result/',cosmetic.views.search_result, name="search_result"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
