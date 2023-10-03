from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects(request):
    # msg = "Hello, you are on projects page"
    # number = 11
    # context = {'message': msg, 'number': number, 
    #           'projectList': projectList}
    projects = Project.objects.all()
    context = {'projectList': projects}
    return render(request, 'projects/projects.html', context = context)

def project(request, pk):
    # projectObj = None
    # for i in  projectList:
    #     if i['id'] == pk:
    #         projectObj = i
    projectObj = Project.objects.get(id = pk)
    return render(request, 'projects/single-project.html', 
                  {'projectObj': projectObj})
    
    
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {"form": form} 
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {"form": form} 
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {"object": project}
    return render(request, 'projects/delete_template.html', context)