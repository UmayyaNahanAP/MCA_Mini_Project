from django.urls import path
from .views import schem

app_name='user'

urlpatterns = [
    path('schems/',schem.index,name='index'),
    path('schems/<int:id>/',schem.details,name='details'),
    path('schems/<int:id>/apply/',schem.schem_apply,name='schem_apply'),
]