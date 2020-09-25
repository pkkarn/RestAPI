from django.urls import path
from api_basic import views
urlpatterns = [
    path('function/', views.article_list, name='function_api'),
    path('function/<int:pk>/', views.article_detail, name='function_api_pk'),
    path('class/', views.ArticleAPIView.as_view(), name='class_api'),
    path('class/<int:id>/', views.ArticleDetail.as_view(), name='class_api_pk'),
    path('generic/', views.GenericAPIView.as_view(), name='generic_api'),
    path('generic/<int:id>/', views.GenericAPIView.as_view(), name='generic_api_pk')

]
