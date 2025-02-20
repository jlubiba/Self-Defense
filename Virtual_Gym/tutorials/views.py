from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
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
    return render(request, 'tutorials/tutorial_home.html', {})
def ttest(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'tutorials/testza.html', context)

@api_view(['GET'])
def index00(request):
    items = Technique.objects.select_related('sub_category').prefetch_related('target').all()
    blevel = request.query_params.get('body_level')
    atypes = request.query_params.get('action_types')
    dlevel = request.query_params.get('difficulty_level')
        
    if atypes:
        items = items.filter(action_types=atypes)
    if blevel:
        items = items.filter(body_level=blevel)
    if dlevel:
        items = items.filter(difficulty_level=dlevel)

    # techniques = TechniqueSerializer(items, many=True)
    context = {
        'techniques': items,
    }
    # return Response(techniques.data)
    return render(request, 'tutorials/written_tutorial_home.html', context)

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
    items = Technique.objects.prefetch_related('target').select_related('sub_category').all()
    category_name = request.query_params.get('category')
    technique_name = request.query_params.get('technique')
    subcategory_name = request.query_params.get('subcategory')
    target_name = request.query_params.get('target')
    target_level = request.query_params.get('target-level')
    action_types = request.query_params.get('action-types')
    body_level = request.query_params.get('body-level')
    difficty_level = request.query_params.get('difficty-level')
    ordering = request.query_params.get('ordering')
    
    if category_name:
        category_name_fields = technique_name.split(',')
        items = items.filter(category__name__in= [*category_name_fields])
    if subcategory_name:
        subcategory_name_fields = subcategory_name.split(',')
        items = items.filter(subcategory__name__in= [*subcategory_name_fields])
    if action_types:
        action_types_fields = action_types.split(',')
        items = items.filter(action_types__in= [*action_types_fields])
    if body_level:
        body_level_fields = body_level.split(',')
        items = items.filter(body_level__in= [*body_level_fields])
    if difficty_level:
        difficty_level_fields = difficty_level.split(',')
        items = items.filter(difficty_level__in= [*difficty_level_fields])
    if target_name:
        target_name_fields = target_name.split(',')
        items = items.filter(target__in= [*target_name_fields])
    if target_level:
        target_level_fields = target_level.split(',')
        items = items.filter(target__body_level__in= [*target_level_fields])
    if technique_name:
        technique_name_fields = technique_name.split(',')
        items = items.filter(name__in= [*technique_name_fields])
        print(items)
    if ordering:
        ordering_fields = ordering.split(',')
        items = items.order_by(*ordering_fields)
    
    for i in items:
        print('-----------')
        print(i)
        print(i.application)
        print(i.action_types)
        print('-----------')
        
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
    
    def list(self, request):
        items = self.queryset
        blevel = request.query_params.get('body_level')
        atypes = request.query_params.get('action_types')
        dlevel = request.query_params.get('difficulty_level')
            
        if atypes:
            items = items.filter(action_types=atypes)
        if blevel:
            items = items.filter(body_level=blevel)
        if dlevel:
            items = items.filter(difficulty_level=dlevel)

        # techniques = TechniqueSerializer(items, many=True)
        context = {
            'techniques': items,
        }
        # return Response(techniques.data)
        return render(request, 'tutorials/written_tutorial_home.html', context)

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

class WelcomeTTutorial(ListView):
    model = Category
    template_name = 'tutorials/TT_home.html'
    context_object_name = 'category_list'
    
class WelcomeVTutorial(ListView):
    model = Category
    template_name = 'tutorials/VT_home.html'
    context_object_name = 'category_list'

class SingleCategoryTTutorial(DetailView):
    model = Category
    template_name = 'tutorials/TT_single_cat.html'
    
    def get_context_data(self, **kwargs):
        current_sub_category = SubCategory.objects.filter(category__id=self.kwargs['pk'])  # Fetches the subcategory for the current category's id
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleCategoryTTutorial, self).get_context_data(**kwargs)
        context['current_sub_category'] = current_sub_category
        context['category_list'] = category_list
        return context

class SingleCategoryVTutorial(DetailView):
    model = Category
    template_name = 'tutorials/VT_single_cat.html'
    
    def get_context_data(self, **kwargs):
        current_sub_category = SubCategory.objects.filter(category__id=self.kwargs['pk'])  # Fetches the subcategory for the current category's id
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleCategoryVTutorial, self).get_context_data(**kwargs)
        context['current_sub_category'] = current_sub_category
        context['category_list'] = category_list
        return context
    
class SingleSubCategoryTTutorial(DetailView):
    model = SubCategory
    template_name = 'tutorials/TT_single_subcat.html'
    context_object_name = 'subcategory_list'
    
    def get_context_data(self, **kwargs):
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleSubCategoryTTutorial, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        return context
    
class SingleSubCategoryVTutorial(DetailView):
    model = SubCategory
    template_name = 'tutorials/VT_single_subcat.html'
    context_object_name = 'subcategory_list'
    
    def get_context_data(self, **kwargs):
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleSubCategoryVTutorial, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        return context
    
    
class SingleTechniqueTTutorial(DetailView):
    model = Technique
    template_name = 'tutorials/TT_technique.html'
    
    def get_context_data(self, **kwargs):
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleTechniqueTTutorial, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        return context
    
class SingleTechniqueComboTTutorial(DetailView):
    model = Technique
    template_name = 'tutorials/TT_technique_combo.html'
    
    def get_context_data(self, **kwargs):
        combo = Combo.objects.get(pk=self.kwargs.get('combo_pk')) # The combo's page pk
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleTechniqueComboTTutorial, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        context['combo'] = combo
        return context
    

class AllCategoryTTutorial(ListView):
    model = Category
    template_name = 'tutorials/TT_all_cat.html'
    context_object_name = 'category_list'
    paginate_by = 3
    
class SingleComboTTutorial(DetailView):
    model = Combo
    template_name = 'tutorials/TT_combo.html'
    
    def get_context_data(self, **kwargs):
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(SingleComboTTutorial, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        return context

class vtest(DetailView):
    model = VideoTutorial
    template_name = 'tutorials/testzb.html'
    category_list = Category.objects.all()
    video_tutorial_list = VideoTutorial.objects.all()
    context_object_name = 'video_tutorial'
    
    def get_context_data(self, **kwargs):
        sub_pk = SubCategory.objects.get(pk=self.kwargs.get('sub_pk'))
        vpk = VideoTutorial.objects.get(id = self.kwargs['pk']).subcategory
        technique_list = Technique.objects.filter(sub_category = vpk)[:4]
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(vtest, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        context['techniques'] = technique_list
        context['sub_pk'] = sub_pk
        return context


def LikedVideoTT(request, pk):
    video = get_object_or_404(VideoTutorial, id = request.POST.get('video_tutorial_id'))
    liked = False
    
    if video.likes.filter(id=request.user.id).exists():
        video.likes.remove(request.user)
        liked = False
    else:
        video.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('tutorials:vtest', args=[str(pk)]))

class AddCommentPostView(CreateView):
    model = Comment
    form_class = CommentForm

class AllComboTTutorial(ListView):
    model = Combo
    template_name = 'tutorials/TT_all_combo.html'
    context_object_name = 'combo_list'
    paginate_by = 6
    ordering = ['-difficulty_level']
    
    def get_context_data(self, **kwargs):
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(AllComboTTutorial, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        return context
    

def FormsPage(request):
    technique_form = techniqueForm()
    category_form = categoryForm()
    subcategory_form = subCategoryForm()
    
    if request.method == 'POST':
        category_form = categoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
    
    context = {
        'technique_form': technique_form,
        'category_form': category_form,
        'subcategory_form': subcategory_form,
        }
    
    return render(request, 'tutorials/add_technique.html', context)
    
class AddCategoryView(CreateView):
    model = Category
    form_class = categoryForm
    template_name = 'tutorials/add_category.html'
    
    def get_context_data(self, **kwargs):
        category_list = Category.objects.all() # Fetches the subcategory for the current category's id
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context['element_list'] = category_list
        return context
    
class AddSubategoryView(CreateView):
    model = subCategory
    form_class = subCategoryForm
    template_name = 'tutorials/add_subcategory.html'
    
    def get_context_data(self, **kwargs):
        subcategory_list = SubCategory.objects.all()
        category_list = Category.objects.all()
        context = super(AddSubategoryView, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        context['element_list'] = subcategory_list
        return context
    
class AddTechniqueView(CreateView):
    model = Technique
    form_class = techniqueForm
    template_name = 'tutorials/add_technique.html'
    
    def get_context_data(self, **kwargs):
        technique_list = Technique.objects.all()
        context = super(AddTechniqueView, self).get_context_data(**kwargs)
        context['element_list'] = technique_list
        return context

class AddComboView(CreateView):
    model = Combo
    form_class = comboForm
    template_name = 'tutorials/add_combo.html'
    
    def get_context_data(self, **kwargs):
        combo_list = Combo.objects.all()
        context = super(AddComboView, self).get_context_data(**kwargs)
        context['element_list'] = combo_list
        return context

class UpdateCategoryView(UpdateView):
    model = Category
    form_class = categoryForm
    template_name = 'tutorials/update_form.html'
    
    def get_context_data(self, **kwargs):
        element_type = 'category'
        context = super(UpdateCategoryView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context
    
class UpdateSubCategoryView(UpdateView):
    model = SubCategory
    form_class = subCategoryForm
    template_name = 'tutorials/update_form.html'
    
    def get_context_data(self, **kwargs):
        element_type = 'subcategory'
        context = super(UpdateSubCategoryView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context
    
class UpdateComboView(UpdateView):
    model = Combo
    form_class = comboForm
    template_name = 'tutorials/update_form.html'
    
    def get_context_data(self, **kwargs):
        element_type = 'combo'
        context = super(UpdateComboView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context
    
class UpdateTechniqueView(UpdateView):
    model = Technique
    form_class = techniqueForm
    template_name = 'tutorials/update_form.html'
    
    def get_context_data(self, **kwargs):
        element_type = 'combo'
        context = super(UpdateTechniqueView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'tutorials/delete_form.html'
    context_object_name = 'element'
    success_url = reverse_lazy('tutorials:add_category') # This is added to redirect to the chosen page with the DeleteView avoid the following error: "No URL to redirect to. Provide a success_url."
    
    def get_context_data(self, **kwargs):
        element_type = 'category'
        context = super(DeleteCategoryView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context

class DeleteSubCategoryView(DeleteView):
    model = SubCategory
    template_name = 'tutorials/delete_form.html'
    context_object_name = 'element'
    success_url = reverse_lazy('tutorials:add_subcategory')
    
    def get_context_data(self, **kwargs):
        element_type = 'subcategory'
        context = super(DeleteSubCategoryView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context

class DeleteComboView(DeleteView):
    model = Combo
    template_name = 'tutorials/delete_form.html'
    context_object_name = 'element'
    success_url = reverse_lazy('tutorials/tutorials:add_combo')
    
    def get_context_data(self, **kwargs):
        element_type = 'combo'
        context = super(DeleteComboView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context

class DeleteTechniqueView(DeleteView):
    model = Technique
    template_name = 'tutorials/delete_form.html'
    context_object_name = 'element'
    success_url = reverse_lazy('tutorials/tutorials:add_technique')
    
    def get_context_data(self, **kwargs):
        element_type = 'technique'
        context = super(DeleteTechniqueView, self).get_context_data(**kwargs)
        context['element_type'] = element_type
        return context