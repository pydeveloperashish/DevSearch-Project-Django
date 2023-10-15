from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects

# Create your views here.
def projects(request):
    projects, search_query = searchProjects(request)
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)
    try:    
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    context = {'projectList': projects, 'search_query': search_query, 'paginator': paginator}
    return render(request, 'projects/projects.html', context = context)

def project(request, pk):
    # projectObj = None
    # for i in  projectList:
    #     if i['id'] == pk:
    #         projectObj = i
    projectObj = Project.objects.get(id = pk)
    return render(request, 'projects/single-project.html', 
                  {'projectObj': projectObj})
    

@login_required(login_url = "login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('account')
        
    context = {"form": form} 
    return render(request, 'projects/project_form.html', context)


@login_required(login_url = "login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('account')
        
    context = {"form": form} 
    return render(request, 'projects/project_form.html', context)


@login_required(login_url = "login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {"object": project}
    return render(request, 'projects/delete_template.html', context)