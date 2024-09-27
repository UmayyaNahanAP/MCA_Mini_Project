from django.urls import path
from .views import schems

app_name='officer'

urlpatterns = [
    path('schems/',schems.index,name='schems'),
    path('schems/create/',schems.create,name='create_schem'),
    path('schems/<int:id>/update/',schems.update,name='update_schem'),
    path('schems/<int:id>/',schems.details,name='details_schem'),
    path('schems/<int:id>/delete/',schems.delete,name='delete_schem'),
]