from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='posts_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('category/<str:string>/', views.Category.as_view(), name='category'),
    path('/reviewContact/', views.ReviewContact.as_view(), name='add_review_contact'),
]