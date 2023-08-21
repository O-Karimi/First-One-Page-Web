from django.shortcuts import render , HttpResponse

# Create your views here.
def base_view(request):
    return render(request , 'website/index.html')