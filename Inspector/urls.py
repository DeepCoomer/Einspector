from django.contrib import admin
from django.urls import path,include
from Inspector import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="Home"),
    path('Fir',views.fir,name="Fir"),
    path('Status',views.status,name="status"),
    path('FirStatus',views.statusdetails,name="FirStatus")
] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

