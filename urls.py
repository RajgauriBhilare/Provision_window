from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ContactEnquiryCreateView, ContactEnquiryViewSet, DataListView, ProductViewSet, ProjectViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'contact', ContactEnquiryViewSet, basename='contact')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactEnquiryCreateView.as_view(), name='contact-create'),
    path('data/', DataListView.as_view(), name='data-list'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
