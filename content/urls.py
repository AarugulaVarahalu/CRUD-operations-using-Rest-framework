from django.urls import path
from .views import contact_details,create_contact,update_contact,delete_contact,view_contact

urlpatterns = [
    path('',contact_details, name='content'),
    path('create_contact/',create_contact,name='create'),
    path('update_contact/<int:id>/', update_contact,name='update'),
    path('delete_contact/<int:id>/', delete_contact,name='delete'),
    path('view_contact/<int:id>/', view_contact,name='view'),
]