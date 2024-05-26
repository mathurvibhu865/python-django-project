from django.urls import path
from .views import ClientList,ClientDetails,ProjectDetails,ProjectList
urlpatterns = [
    path('client/',ClientList.as_view(),name='client-list'),
    path('client/<int:id>',ClientDetails.as_view(),name='client-details'),
    path('project/',ProjectList.as_view(),name='project-list'),
    path('project/<int:id>',ProjectDetails.as_view(),name='project-details'),

]