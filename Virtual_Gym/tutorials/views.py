from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, throttle_classes, api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from .permissions import *
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the welcoming page!")

def test(request):
    techniqueform = techniqueForm()
    targetform = targetForm()
    if request.method == 'POST':
        form = techniqueForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'techniqueform':techniqueform,
        'targetform':targetform,
    }
    return render(request, 'tutorials/testform.html', context)

@api_view()
def TechniqueGenerator(request, *args, **kwargs):
    items = Technique.objects.prefetch_related('target').select_related('sub_category').filter(*args, **kwargs)
    category_name = request.query_params.get('category')
    subcategory_name = request.query_params.get('subcategory')
    target_name = request.query_params.get('target')
    target_level = request.query_params.get('target-level')
    action_types = request.query_params.get('action-types')
    body_level = request.query_params.get('body-level')
    difficty_level = request.query_params.get('difficty-level')
    ordering = request.query_params.get('ordering')
    
    if category_name:
        items = items.filter(category__name=category_name)
    if subcategory_name:
        items = items.filter(subcategory__name=subcategory_name)
    if action_types:
        items = items.filter(action_types=action_types)
    if body_level:
        items = items.filter(body_level=body_level)
    if difficty_level:
        items = items.filter(difficty_level=difficty_level)
    if category_name:
        items = items.filter(category__name=category_name)
    if target_name:
        items = items.filter(target__name=target_name)
    if target_level:
        items = items.filter(target__body_level=target_level)
    if ordering:
        ordering_fields = ordering.split(',')
        items = items.order_by(*ordering_fields)
    
    
    serialized_data = TechniqueSerializer(items, many=True)
        
    return Response(serialized_data.data)

class category(viewsets.ModelViewSet):
    queryset = Category.objects.select_related('added_by').all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsTutorialManagerPermission | IsGeneralManagerPermission]
        else:
            permission_classes = [IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]

class tag(viewsets.ModelViewSet):
    queryset = Tag.objects.select_related('added_by').all()
    serializer_class = TagSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsTutorialManagerPermission | IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]

class subCategory(viewsets.ModelViewSet):
    queryset = SubCategory.objects.select_related('category', 'added_by').all()
    serializer_class = SubCategorySerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsTutorialManagerPermission| IsGeneralManagerPermission | IsAdminUser]
        
        return [permission() for permission in permission_classes]

class target(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsTutorialManagerPermission | IsGeneralManagerPermission]
        else:
            permission_classes = [IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]

class technique(viewsets.ModelViewSet):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsTutorialManagerPermission | IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]

class combo(viewsets.ModelViewSet):
    queryset = Combo.objects.prefetch_related('technique', 'target').all()
    serializer_class = ComboSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsTutorialManagerPermission | IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]

class textTutorial(viewsets.ModelViewSet):
    queryset = TextTutorial.objects.all()
    serializer_class = TextTutorialSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthorPermission | IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]

class videoTutotial(viewsets.ModelViewSet):
    queryset = VideoTutorial.objects.all()
    serializer_class = VideoTutorialSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthorPermission | IsGeneralManagerPermission]
        
        return [permission() for permission in permission_classes]