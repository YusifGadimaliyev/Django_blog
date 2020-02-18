from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post, useful
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.db.models import Q


# Create your views here.


def homePage(request):
    links = useful.objects.all().order_by('-pub_date')[:3]
    object_list = Post.objects.all().order_by('-pub_date')
    most_read = Post.objects.all().order_by('-show')[:3]
    most = Post.objects.all()
    query = request.GET.get('q')
    if query:
        object_list = object_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
            ).distinct()
    paginator = Paginator(object_list, 5)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {
                                        'page': page,
                                        'links': links,
                                        'most_read': most_read,
                                        'post_list': post_list
                                        })


def postDetail(request, pk):
    links = useful.objects.all().order_by('-pub_date')[:3]
    post = get_object_or_404(Post, pk=pk)
    post.show += 1
    post.save()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'links': links,
        'form': form,
    }
    return render(request, 'post.html', context)

