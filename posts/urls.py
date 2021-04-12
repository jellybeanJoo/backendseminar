from django.urls import path
from posts import views 

urlpatterns=[
    # path('',views.index,name='index'),
    path('GET/<int:el>/', views.crud_get),
    path('POST/<int:el>/',views.crud_post),
    path('PUT/<int:el>/',views.crud_put),
    path('DELETE/<int:el>/',views.crud_delete),
]