from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #projects
    path('projects', views.projects_index, name='index'),
    path('projects/<int:project_id>/', views.projects_detail, name='detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete', views.ProjectDelete.as_view(), name='projects_delete'),
    #color schemes
    path('colors/scheme/<int:scheme_id>/', views.color_scheme_detail, name='color_scheme_detail'),
    path('colors/scheme/create/', views.ColorSchemeCreate.as_view(), name='color_scheme_create'),
    path('colors/scheme/<int:pk>/update', views.ColorSchemeUpdate.as_view(), name='color_scheme_update'),
    path('colors/scheme/<int:pk>/delete', views.ColorSchemeDelete.as_view(), name='color_scheme_delete'),
    #colors
    path('colors', views.colors_index, name='color_index'),
    path('colors/<int:color_id>/', views.color_detail, name='color_detail'),
    path('colors/create/', views.ColorsCreate.as_view(), name='colors_create'),
    path('colors/<int:pk>/update', views.ColorUpdate.as_view(), name='color_update'),
    path('colors/<int:pk>/delete', views.ColorDelete.as_view(), name='color_delete'),
    #users
    path('accounts/signup/', views.signup, name='signup'),
    
]
