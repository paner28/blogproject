from django.urls import path
from .views import BlogList,BlogDetail,BlogCreate,BlogDelete,BlogUpdate,indexview,skillview,sportview,BlogTopic,BlogAnime,BlogMath,BlogFood

urlpatterns = [
    path('', BlogList.as_view(), name='home'),
    path('index/', indexview, name="index"),
    path('skill/', skillview, name="skill"),
    path('anime/', BlogAnime.as_view(), name="anime"),
    path('sport/', sportview, name="sport"),
    path('math/', BlogMath.as_view(), name="math"),
    path('food/', BlogFood.as_view(), name="food"),
    path('topic/<str:parameter>', BlogTopic.as_view(), name='topic'),
    path('detail/<int:pk>', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),
]