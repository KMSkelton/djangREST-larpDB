from django.urls import path, include
from . import views

urlpatterns = [
  path('api/attribute/', views.AttributeListCreate.as_view() ),
  path('api/attribute/<int:pk>', views.AttributeDetail.as_view() ),
  path('rest-auth/', include('rest_auth.urls')),
]