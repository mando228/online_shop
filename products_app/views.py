from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "index.html")

def pruducts(request, category_id=None, page=1):
    if category_id:
        product = Product.objects.filter(category_id=category_id)
    else:
        product = Product.objects.all()
    
    category = ProductCategory.objects.all()
    per_page = 3
    paginator = Paginator(product, per_page)
    paginated_products = paginator.page(page)
    context =  {
        "products": paginated_products,
        "categories": category,
        }
    
    return render(request, "products.html", context)

@login_required
def add_to_basket(request,product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user = request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quanity=1)
    
    else:
        baskets=baskets.first()
        baskets.quanity+=1
        baskets.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def del_from_basket(request, bask_id):
    baskets = Basket.objects.filter(user = request.user, id=bask_id)
    baskets.delete()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
