from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('TestApp/', views.TestApp,
        name="TestApp"
    ),
    path('create/contact/', views.CreateContact,
        name="Create_Contact"
    ),
    path('create/ticket/', views.CreateTiket,
        name="Create_Ticket"
    ),
    path('list/tickets/', views.ListTikets,
        name="List_Ticket"
    ),
    path('list/contacts/', views.ListContacts,
        name="List_Contacts"
    )
]
 