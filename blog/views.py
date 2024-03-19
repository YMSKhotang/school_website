from django.shortcuts import render, redirect
from blog.models import Category, Comment, Post, Contact,Gallery
from django.http import HttpResponseRedirect
from .forms import ContactForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#home
def home(request):
    return render (request,'blog/homepage.html')

#blog
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)

#blog_category
def blog_category(request,category):
    posts = Post.objects.filter(categories__name__contains = category).order_by("-created_on")
    context = {
        "category":category,
        "posts":posts,
    }
    return render(request, "blog/blog_category.html", context)

#blog_detail
def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    #after form
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        

    comments = Comment.objects.filter(post=post)

    #before form
    context = {
        "post":post,
        "comments":comments,  
        #after form
        'form':CommentForm(),
    }
    return render(request, "blog/blog_detail.html",context)

#contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Your message was sent successfully!')
            
            # Create a new empty form
            form = ContactForm()

            return render(request, 'blog/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})


# search function


def search(request):
    query=request.GET['query']

    if len(query)>78:
        myPosts=Post.objects.none()
    else:
        myPostsTitle= Post.objects.filter(title__icontains=query)
        myPostsContent =Post.objects.filter(body__icontains=query)
        myPosts=  myPostsTitle.union(myPostsContent)

    '''
    if myPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    '''
    
    params={'allPosts': myPosts, 'query': query}

    return render(request, 'blog/search.html', params)

#gallery
def gallery(request):
    images = Gallery.objects.all().order_by("-created_date")

    # Paginate the list of images
    paginator = Paginator(images, 9)  # Change 9 to the desired number of images per page

    # Get the current page number from the request, default to 1
    page_number = request.GET.get('page', 1)

    try:
        # Retrieve the images for the current page
        images_page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        images_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        images_page = paginator.page(paginator.num_pages)
    context={
        'images_page':images_page
    }
    
    return render (request,'blog/gallery.html',context)

