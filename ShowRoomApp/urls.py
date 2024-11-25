from django.urls import path
from .import views

urlpatterns = [
   path('', views.home,name='my_home'),
   path('attendees/', views.attendees,name='my_attendees'),
#    path('participants/', views.participants,name='my_participants'),
#    path('attendees/<int:pk>/', views.attendee_detail,name='my_attendee_detail'),
   path('attendees_add/', views.attendees_add,name='my_attendees_add'),
#    path('attendees/<int:pk>/update/', views.attendee_update,name='my_attendee_update'),
]
