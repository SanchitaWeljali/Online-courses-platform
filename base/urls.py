from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', shop_views.index, name='home'),
    path('api/', include('api.urls'))
]
