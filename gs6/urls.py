from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('podcast/', views.podcast_api),
    path('get_audio/<str:audio_type>/<int:audio_id>/', views.final_api, name="get_id"),
    path('get_audio/<str:audio_type>/', views.final_api, name="get"),
    path('post_audio/<str:audio_type>/', views.final_api, name="create"),
    path('update_audio/<str:audio_type>/<int:audio_id>/', views.final_api, name="update"),
    path('delete_audio/<str:audio_type>/<int:audio_id>/', views.final_api, name="delete"),
    path('song/', views.SongAPI.as_view()),
    path('story/', views.StoryAPI.as_view()),
]
