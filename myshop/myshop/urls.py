from shop import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('catalog/', views.catalog, name='catalog'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
