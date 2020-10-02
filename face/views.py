from django.shortcuts import render, HttpResponse, redirect
from django.contrib.staticfiles.storage import staticfiles_storage
import boto3
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from .models import ImageModel
from django.conf import settings
from .detect_face import detect_face
from django.core.paginator import Paginator

def home(request): 
    allimages = ImageModel.objects.all().order_by('-id')
    paginator= Paginator(allimages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'face/index.html',{'page_obj': page_obj, 'MEDIA_URL': settings.MEDIA_URL})


def upload_image(request):
    if request.method == "GET":
        form = ImageForm()
        return render(request, 'face/upload.html', {'form': form})

    if request.method == "POST":
        print(request.POST)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'face/upload.html', {'form': form})



def analyze(request, pk):
    image= ImageModel.objects.get(id=pk)
    image_url = str(settings.BASE_DIR)+image.image.url
    celebrity, response = detect_face(image_url) 
    print(celebrity)
    return render(request, 'face/analyze.html', {'res': response,'celebrity':celebrity, 'image': image } )
    return HttpResponse('ok')

        

