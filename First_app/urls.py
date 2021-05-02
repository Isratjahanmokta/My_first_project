from django.conf.urls import url
from django.urls import path
from First_app import views

app_name = "First_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_album/', views.album_form, name='album_form'),
    path('Add_musician/', views.musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name ='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name ='edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name ='delete_album'),
]
