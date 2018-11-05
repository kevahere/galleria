from django.shortcuts import render
from .models import Images,Location,Category
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    images = Images.all_pics()
    locations = Location.objects.all()
    return render(request,'index.html',{'images':images,'locations':locations})

def search_results(request):
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_category = Category.search_category(search_term)
        message = f'(searched_term)'

        return render(request,'search.html',{'message': message,'category':searched_category})

    else:
        message = "You have to search for something!"
        return render(request,'search.html',{'message': message,'category':searched_category})

def location(request, location):
    locations = Location.objects.all()
    try:
        pics = Images.filter_by_loc(location)
    except Images.DoesNotExist:
        raise Http404()

    return render(request, 'location.html', {'pics': pics, 'locations': locations})


def category(request, category):
    locations = Location.objects.all()
    try:
        pics = Images.filter_by_category(category)
    except Images.DoesNotExist:
        raise Http404()

    return render(request, 'location.html', {'pics': pics, 'locations': locations})
