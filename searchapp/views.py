from django.shortcuts import render
from shopping.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    products = None
    query = None
    if request.method == 'POST':
        query = request.POST.get('searchkey')
        products = Product.objects.all().filter(Q(name__contains = query) | Q(description__contains = query))
    else:
        query = None
    return render(request,'search.html',{'query':query,'products':products})