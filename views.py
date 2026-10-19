from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ContactEnquiry, Product, Project
from .serializers import ContactEnquirySerializer, ProductSerializer, ProjectSerializer, UserSerializer

User = get_user_model()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DataListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        records = [
            {
                'id': f'product-{product.id}',
                'type': 'Product',
                'title': product.name,
                'detail': product.category,
                'created_at': product.created_at,
            }
            for product in Product.objects.all().order_by('-created_at')
        ]
        records += [
            {
                'id': f'project-{project.id}',
                'type': 'Project',
                'title': project.title,
                'detail': project.location,
                'created_at': project.created_at,
            }
            for project in Project.objects.all().order_by('-created_at')
        ]
        records += [
            {
                'id': f'enquiry-{enquiry.id}',
                'type': 'Enquiry',
                'title': enquiry.subject,
                'detail': enquiry.name,
                'created_at': enquiry.created_at,
            }
            for enquiry in ContactEnquiry.objects.all().order_by('-created_at')
        ]
        return Response(records)


class ContactEnquiryCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactEnquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactEnquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactEnquiry.objects.all().order_by('-created_at')
    serializer_class = ContactEnquirySerializer
