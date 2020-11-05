from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectCreationForm

@login_required
def home(request):
    """Dashboard route"""

    # Display 5 last projects
    projects = Project.objects.filter(users=request.user).order_by('-date_created').all()[:5]
    

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
    
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)

        if form.is_valid():
            form.save(request)
            return redirect('list_projects')

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


@login_required
def detail_project(request, id):
    """Main project page"""

    project = get_object_or_404(Project, id=id)

    context = {
        'project': project
    }

    return render(request, "core_app/detail-project.html", context)