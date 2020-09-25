from django.urls import path, include
from api_basic import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('gen_viewset', views.ArticleViewSet, basename='article')
router.register('mod_viewset', views.ArticleModalViewSet, basename='article_modal')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('function/', views.article_list, name='function_api'),
    path('function/<int:pk>/', views.article_detail, name='function_api_pk'),
    path('class/', views.ArticleAPIView.as_view(), name='class_api'),
    path('class/<int:id>/', views.ArticleDetail.as_view(), name='class_api_pk'),
    path('generic/', views.GenericAPIView.as_view(), name='generic_api'),
    path('generic/<int:id>/', views.GenericAPIView.as_view(), name='generic_api_pk')
]
