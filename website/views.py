from django.shortcuts import render , HttpResponse
from django.templatetags.static import static

# Create your views here.
def base_view(request):
    why_us_image_url = static('img/why-us.png')
    context = {
        'why_us_image_url': why_us_image_url
    }    
    return render(request , 'website/index.html', context)