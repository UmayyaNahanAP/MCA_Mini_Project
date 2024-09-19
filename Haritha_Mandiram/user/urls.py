from django.urls import path
from .views import schems

app_name='user'

urlpatterns = [
    path('schems/',schems.index,name='index'),
    path('schems/<int:id>/',schems.details,name='details'),
    # path('schems/apply/',schems.schem_apply,name='schem_apply'),
]