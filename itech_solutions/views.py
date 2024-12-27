from django.shortcuts import render, redirect
from .models import Software

def home(request):
    softwares = Software.objects.all()
    return render(request, 'index.html', {'softwares': softwares})


def upload_software(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        uploaded_file = request.FILES['file']

        if not uploaded_file.name.endswith('.exe'):
            return render(request, 'software_form.html', {
                'error': 'Only .exe files are allowed.',
            })

        # Save data to the database
        software = Software(name=name, description=description, file=uploaded_file)
        software.save()

        return redirect('software_list')  # Redirect to the list page after upload

    return render(request, 'software_form.html')



def software_list(request):
    softwares = Software.objects.all()
    return render(request, 'list.html', {'softwares': softwares})



from django.shortcuts import get_object_or_404
def update_software(request, id):
    software = get_object_or_404(Software, id=id)  # Get the software object by id

    if request.method == 'POST':
        software.name = request.POST.get('name')
        software.description = request.POST.get('description')

        # Handle file upload
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            software.file = uploaded_file  # Replace with the new file

        software.save()  # Save the updated software instance
        return redirect('software_list')  # Redirect to the software list page after updating

    return render(request, 'update_form.html', {'software': software})



def delete_software(request, id):
    software = get_object_or_404(Software, id=id)
    software.delete()
    return redirect('software_list')  # Redirect to the software list

from django.shortcuts import render
from .models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import*

class getsoftware(APIView):
    def get(self,request):
        software= Software.objects.all()
        serializers = SoftwareSerializer(software,many=True)
        return Response(serializers.data)

# class getstudentById(APIView):
#     def get(self,request,id):
#         Student= Students.objects.get(id = id)
#         serializers = StudentSerilizers(Student)
#         return Response(serializers.data)

class createsoftware(APIView):
    def post(self,request):
        serializer = SoftwareSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class updatesoftware(APIView):
    def put(self,request,id):
        software = Software.objects.get(id=id)
        serializer = SoftwareSerializer(software,data = request.data,partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({"message":"updated suceess"})

class deletesoftware(APIView):
    def delete(self,request,id):
        software =Software.objects.get(id = id)
        software.delete()
        return Response({"message":"deleted successfully"})

