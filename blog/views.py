from django.shortcuts import render, get_object_or_404
from homepage.models import HomepageInfo
from blog.models import Post


def blog(request):
    data = HomepageInfo.objects.all().first()
    post = Post.objects.all().order_by('-id')
    context = {'data':data,'post':post}
    return render(request, 'blog.html', context)



def blog_single(request, id):
    data = HomepageInfo.objects.all().first()
    post = get_object_or_404(Post, id=id)
    try:
        previous = get_object_or_404(Post, id=(id-1))
    except:
        previous = None
    try:
        next = get_object_or_404(Post, id=(id+1))
    except:
        next = None
    context = {'data':data,'post':post,'previous':previous,'next':next}
    return render(request, 'blog-single.html', context)

