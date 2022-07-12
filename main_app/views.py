from urllib import request
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from main_app.forms import ColorSchemeForm, ProjectsForm
from .models import Project, Color, ColorScheme
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#projects
@login_required
def projects_index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'projects/index.html', {"projects": projects})

@login_required
def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'projects/detail.html', {"project": project})

@login_required
def colors_index(request):
    colors = Color.objects.filter(user=request.user)
    schemes = ColorScheme.objects.filter(user=request.user)
    context = {"colors": colors, "schemes": schemes}
    return render(request, 'colors/colors_index.html', context )

@login_required
def color_detail(request, color_id):
    color = Color.objects.get(id=color_id)
    return render(request, 'colors/color_detail.html', {"color": color})

@login_required
def color_scheme_detail(request, scheme_id):
    scheme = ColorScheme.objects.get(id=scheme_id)
    color = Color.objects.filter(user=request.user)
    return render(request, 'colors/color_scheme_detail.html', {"scheme": scheme, "color": color})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'main_app/project_form.html'
    form_class = ProjectsForm
    success_url = '/projects'

    def get_form_kwargs(self):
        kwargs = super(ProjectCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'main_app/project_form.html'
    form_class = ProjectsForm
    success_url = '/projects'

    def get_form_kwargs(self):
        kwargs = super(ProjectUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/projects'

class ColorsCreate(LoginRequiredMixin, CreateView):
    model = Color
    fields = ['name', 'hex']
    success_url = '/colors'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ColorUpdate(LoginRequiredMixin, UpdateView):
    model = Color
    fields = ['name', 'hex']
    success_url = '/colors'

class ColorDelete(LoginRequiredMixin, DeleteView):
    model = Color
    success_url = '/colors'

# class ColorSchemeCreate(LoginRequiredMixin, CreateView):
#     model = ColorScheme
#     fields = ['name', 'color']
#     success_url = '/colors'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

class ColorSchemeCreate(LoginRequiredMixin, CreateView):
    template_name = 'main_app/colorscheme_form.html'
    form_class = ColorSchemeForm
    success_url = '/colors'

    def get_form_kwargs(self):
        kwargs = super(ColorSchemeCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ColorSchemeUpdate(LoginRequiredMixin, UpdateView):
    model = ColorScheme
    template_name = 'main_app/colorscheme_form.html'
    form_class = ColorSchemeForm
    success_url = '/colors'

    def get_form_kwargs(self):
        kwargs = super(ColorSchemeUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ColorSchemeDelete(LoginRequiredMixin, DeleteView):
    model = ColorScheme
    success_url = '/colors'