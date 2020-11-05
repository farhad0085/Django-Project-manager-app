from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Card, CardItem, Project
from .forms import ProjectCreationForm, CardCreationForm


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
            project = form.save(request)
            return redirect('detail_project', project.id)

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


@login_required
def delete_project(request, id):
    """For delete a project"""

    try:
        project = Project.objects.get(id=id)
        if not request.user in project.users.all():
            return render(request, 'page-403.html')
        
        project.delete()
        return redirect('list_projects')
    except Project.DoesNotExist:
        return render(request, "page-404.html")
    except Exception as e:
        print("Error", e)
        return render(request, "page-500.html")



@login_required
def create_card(request, project_id):
    """Create new card page"""

    form = CardCreationForm()

    try:
        project = Project.objects.get(id=project_id)

        if not request.user in project.users.all():
            return render(request, 'page-403.html')

    except Project.DoesNotExist:
        return render(request, 'page-404.html')

    if request.method == 'POST':
        form = CardCreationForm(request.POST)

        if form.is_valid():
            form.save(request, project)
            return redirect('detail_project', project_id)

    context = {
        'form': form
    }

    return render(request, "core_app/create-card.html", context)


@login_required
def delete_card(request, project_id, card_id):
    """Delete card page"""

    try:
        project = Project.objects.get(id=project_id)
        card = Card.objects.get(id=card_id)

        if not request.user in project.users.all():
            return render(request, 'page-403.html')
        
        card.delete()
        return redirect('detail_project', project_id)

    except Project.DoesNotExist:
        return render(request, 'page-404.html')

    except Card.DoesNotExist:
        return render(request, 'page-404.html')


@login_required
def create_card_item(request, project_id, card_id):
    """Create new card item"""
    
    try:
        project = Project.objects.get(id=project_id)
        card = Card.objects.get(id=card_id)

        if not request.user in project.users.all():
            return render(request, 'page-403.html')
        
        if request.method == 'POST':
            title = request.POST.get('title')
            CardItem.objects.create(
                title=title,
                created_by=request.user,
                card=card
            )
            return redirect('detail_project', project_id)

        else:
            return render(request, 'page-403.html')

    except (Project.DoesNotExist, Card.DoesNotExist):
        return render(request, 'page-404.html')
    except:
        return render(request, 'page-500.html')


@login_required
def delete_card_item(request, project_id, card_item_id):
    """Delete card item route"""
    
    try:
        project = Project.objects.get(id=project_id)
        card_item = CardItem.objects.get(id=card_item_id)

        if not request.user in project.users.all():
            return render(request, 'page-403.html')
        
        card_item.delete()
        return redirect('detail_project', project_id)

    except (Project.DoesNotExist, CardItem.DoesNotExist):
        return render(request, 'page-404.html')
    except:
        return render(request, 'page-500.html')