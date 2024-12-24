
# VIEWS
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Software

# View for rendering the template
def software_list(request):
    softwares = Software.objects.all()
    return render(request, 'add_softwares.html', {'softwares': softwares})

# View to handle adding software
def add_software(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        file = request.FILES.get('file')  # Use .get() to avoid KeyError

        if not file:  # Check if file is provided
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        Software.objects.create(
            name=name,
            description=description,
            file=file
        )
        return redirect('software_list')
    return JsonResponse({'error': 'Invalid request'}, status=400)


# View to handle deleting software
def delete_software(request, id):
    software = get_object_or_404(Software, id=id)
    software.delete()
    return redirect('software_list')

# View to handle updating software
def update_software(request, id):
    software = get_object_or_404(Software, id=id)
    if request.method == 'POST':
        software.name = request.POST['name']
        software.description = request.POST['description']
        if 'file' in request.FILES:
            software.file = request.FILES['file']
        software.save()
        return redirect('software_list')
    return JsonResponse({'error': 'Invalid request'}, status=400)
