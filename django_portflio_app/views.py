from django.shortcuts import render

# Create your views here.
def home(request):
    diction ={}
    return render (request , 'django_portfolio_app/index.html',context=diction)
