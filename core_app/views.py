from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectCreationForm

@login_required
def home(request):
    """Dashboard route"""

    # TODO: Display 5 last projects
    projects = Project.objects.filter(users=request.user).order_by('-date_created').all()
    

    context = {
        'segment': 'index',
        'projects': projects
    }

    return render(request, "index.html", context)



@login_required
def pages(request):

    context = {}
    try:
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        return render(request, load_template, context)
        
    except:
        return render(request, 'page-500.html', context)


@login_required
def create_project(request):
    form = ProjectCreationForm()
    
    context = {
        'segment': 'project-create',
        'form': form
    }

    return render(request, "core_app/create-project.html", context)



@login_required
def list_projects(request):
    """Display all projects"""

    # Display all projects by current user
    projects = Project.objects.filter(users=request.user).order_by('-date_created').all()
    

    context = {
        'segment': 'project-all',
        'projects': projects
    }

    return render(request, "core_app/all-projects.html", context)