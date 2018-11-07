from django.shortcuts import render

def post_list(request):
    return render(request, 'post/post_list.html', {})

def post_list_mobile(request):
    return render(request, 'post/post_list_mobile.html', {})