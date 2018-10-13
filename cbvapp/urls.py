from django.urls import path
from cbvapp import views

app_name='cbvapp'

urlpatterns = [
    path('',views.collageList.as_view(),name='list'),
    path('<int:pk>/',views.collageDetail.as_view(),name='detail'),
]
