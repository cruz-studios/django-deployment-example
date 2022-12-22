from django.shortcuts import render

# Create your views here.
#THE PATH FILE FOR THE RENDER FUNCTION IS JUST THE FILE PATH UNDER TEMPLATES
#TO GET TO THE HTML FILE THAT YOU WANT THE VIEW TO SHOW
def index(request):
    context_dict = {'text': 'hello world','number':100}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
