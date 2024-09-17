from django.urls import path
from .views import schems

app_name='officer'

urlpatterns = [
    path('schems/',schems.index,name='index'),
    path('schems/create/',schems.create,name='create'),
    path('schems/<int:id>/update/',schems.update,name='update'),
    path('schems/<int:id>/',schems.details,name='details'),
    path('schems/<int:id>/delete/',schems.delete,name='delete'),
   
]
