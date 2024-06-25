from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.http import HttpResponse
from django.http import JsonResponse
import logging
from decimal import Decimal
import openpyxl
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    # return JsonResponse({'posts': posts})

    # Rendering the content at the file directory of templates! 
    return render(request, 'blog/DataFrame.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Rendering the content at the file directory of templates! 
    return render(request, 'blog/DataFrame.html', {'post': post})


# React API endpoint
def price_category(request):
    posts = Post.objects.all()
    price_filter = request.GET.get('price_filter', None)
    
    if price_filter == 'lac':
        filtered_posts = posts.filter(price__contains='Lac')
    elif price_filter == 'cr':
        filtered_posts = posts.filter(price__contains='Cr')
    else:
        filtered_posts = posts

    filtered_posts_list = list(filtered_posts.values())
    # return render(request, 'blog/Pricefilter.html',{'posts':filtered_posts_list})
    return JsonResponse({'posts': filtered_posts_list})


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


# def price_category(request, *args, **kwargs):
#     # Retrieve all posts ordered by created_at descending
#     posts = Post.objects.all().order_by('-created_at')

#     # Initialize an empty list to store posts with prices in 'Lac'
#     lac_posts = []

#     # Iterate through each post
#     for post in posts:
#         # Check if the price string contains 'Lac'
#         if 'Lac' in post.price:
#             lac_posts.append(post)

#     return render(request, 'blog/price_category.html', {'posts': lac_posts})



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

