from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import HttpResponse
from .models import Post
from django .utils import timezone
from .forms import PostForm
import datetime

# Create your views here.



def task(request):
    post=Post.objects.filter(Create_date__lte=timezone.now()).order_by('-Create_date')
    result = {'key':post}
    return render(request, 'App/index.html', result)


def new_task(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('task')
    else:
        form = PostForm()
    return render(request, 'App/new_task.html', {'form_data': form})

def del_task(request, pk):
    post_data = get_object_or_404(Post, pk=pk)
    post_data.delete()
    return redirect('/')

def status(request, pk):
    post_data = get_object_or_404(Post, pk=pk)
    if post_data.Status == True:
        status_active = Post.objects.filter(pk=pk).update(Status=False)
    else:
        status_active = Post.objects.filter(pk=pk).update(Status=True)
    return redirect('/')



















