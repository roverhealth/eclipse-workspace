from django.conf.urls import url
from . import views

# edit_pet
 
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    #url(r'^petProfile/edit/$', edit_pet.as_view(), name='edit_pet')
    url(r'^$', views.PetListView.as_view(), name='pet_changelist'),
    url(r'^add/$', views.PetCreateView.as_view(), name='pet_add'),
    url('<int:pk>/', views.PetUpdateView.as_view(), name='pet_change'),
    url('ajax/load-cities/', views.load_breeds, name='ajax_load_breeds'),
    ]