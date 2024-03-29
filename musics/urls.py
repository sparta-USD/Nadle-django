from django.urls import path
from musics import views

urlpatterns = [
    path('<int:music_id>/reviews/', views.ReviewView.as_view(), name='review_view'),
    path('reviews/<int:review_id>/', views.ReviewDetailView.as_view(), name='review_detail_view'),
    path('', views.MusicView.as_view(), name='music_view'),
    path('recommend/', views.MusicRecommandView.as_view(), name='music_recommend_view'),
    path('<int:music_id>/', views.MusicDetailView.as_view(), name='music_detail_view'),
    path('random/', views.MusicRandomView.as_view(), name='music_random_view'),
]
