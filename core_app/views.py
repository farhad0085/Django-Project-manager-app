from .models import Project
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    projects = Project.objects.filter(users=request.user).all()

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