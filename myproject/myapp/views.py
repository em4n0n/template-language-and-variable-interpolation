from django.shortcuts import render

# Create your views here.
def index(request, name):
    context={'name': name}
    return render(request, 'index.html', context)

# def index(request):
#     context={'user': 'admin'}
#     return render(request, 'index.html', context)

def myview(request):
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    return render(request, 'langs.html', {'lang':langs})

