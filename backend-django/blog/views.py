from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.http import HttpResponse
from django.http import JsonResponse
import logging
from decimal import Decimal
import openpyxl
from .forms import PostForm
import googlemaps
from django.conf import settings

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    # return JsonResponse({'posts': posts})

    # Rendering the content at the file directory of templates! 
    return render(request, 'blog/DataFrame.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Rendering the content at the file directory of templates! 
    return render(request, 'blog/DataFrame.html', {'post': post})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})



# Actions-View functionality
def delete(request, pk, *args, **kwargs):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return redirect('post_list')
    

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.name = request.POST.get('name')
        post.price = request.POST.get('price')
        post.floor = request.POST.get('floor')
        post.save()

        return redirect('post_list')  # Redirect to post detail with updated post's pk

    return render(request, 'blog/edit_post.html', {'post': post})


# React Pricefilter endpoint
def pricefilter(request):
    posts = Post.objects.all()
    price_filter = request.GET.get('price_filter', None)
    
    if price_filter == 'lac':
        filtered_posts = posts.filter(price__contains='Lac')
    elif price_filter == 'cr':
        filtered_posts = posts.filter(price__contains='Cr')
    else:
        filtered_posts = posts

    filtered_posts_list = list(filtered_posts.values())
    return render(request, 'blog/Pricefilter.html',{'posts':filtered_posts_list})
    # return JsonResponse({'posts': filtered_posts_list})



def download_posts_excel(request):
    # Create an in-memory workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Posts'

    # Define the header
    headers = ['Property ID', 'Name', 'Price', 'Beds', 'Floor', 'Furnishing', 'Super Areas']
    sheet.append(headers)

    # Query the posts
    posts = Post.objects.all().values_list(
        'property_id', 'name', 'price', 'beds', 'floor', 'furnishing', 'super_areas','Image_url'
    )

    # Append data to the sheet
    for post in posts:
        sheet.append(post)

    # Save the workbook to a response object
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=posts.xlsx'
    workbook.save(response)

    return response

def contact(request, *args, **kwargs):
    posts = Post.objects.all().order_by('-created_at')
    print(args, kwargs)  # Used for get & post request details
    print(request.user)  # Used for Authentication
    my_context = {
        "my_title": "It's about me",
        "my_number": [234, 672, 643, 872, 'abc'],
        "posts": posts,  # Correct key for posts
    }
    # return JsonResponse({"my_info": my_context})
    return render(request, 'blog/contact.html', my_context)

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    my_context = {
        "my_title": "It's about me",
        "my_number": [234, 672, 643, 872, 'abc'],
        "posts": posts,  # Correct key for posts
    }
    return render(request, 'blog/home.html', my_context)

# def property_map_view(request):
#     gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    
#     # Example property data with landmark and addressLocality
#     properties = [
#         {'name': 'Property 1', 'landmark': 'Lajwanti Garden, New Delhi', 'address': 'Lajwanti Garden, Janakpuri'},
#         {'name': 'Property 2', 'landmark': 'Sector 18 Dwarka, New Delhi', 'address': 'Sector 18 Dwarka'},
#         {'name': 'Property 3', 'landmark': 'Geeta Colony, New Delhi', 'address': 'Geeta Colony'},
#         {'name': 'Property 4', 'landmark': 'Karol Bagh, New Delhi', 'address': 'Karol Bagh'},
#         {'name': 'Property 5', 'landmark': 'Sector 14 Rohini, New Delhi', 'address': 'Sector 14 Rohini'},
#         {'name': 'Property 6', 'landmark': 'Paschim Vihar Block B3, New Delhi', 'address': 'Block B3 Paschim Vihar'},
#         {'name': 'Property 7', 'landmark': 'Chandra Nagar, New Delhi', 'address': 'Chander Nagar Krishna Nagar'},
#     ]

#     for prop in properties:
#         geocode_result = gmaps.geocode(prop['address'])
#         if geocode_result and len(geocode_result) > 0:
#             location = geocode_result[0]['geometry']['location']
#             prop['lat'] = location['lat']
#             prop['lng'] = location['lng']
#         else:
#             prop['lat'] = None
#             prop['lng'] = None

#     context = {
#         'properties': properties,
#         'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
#     }
    
#     return render(request, 'blog/property_map.html', context)