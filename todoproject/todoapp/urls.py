from django.urls import path
from .import views


urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cblv/',views.listview.as_view(),name='cblv'),
    path('cbdv/<int:pk>/',views.detailview.as_view(),name='cbdv'),
    path('cbuv/<int:pk>/',views.updateview.as_view(),name='cbuv'),
    path('cbdeleteview/<int:pk>/',views.deleteview.as_view(),name='cbdeleteview'),

]