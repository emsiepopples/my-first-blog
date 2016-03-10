from django.shortcuts import render

def post_list(request):
    return render(request, 'brian/post_list.html', {})