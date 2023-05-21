from typing import Any, Dict
from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.decorators import login_required

# def Index(request):
#     context = {
#         "title" : "wellcome"
#     }
#     return(request, "index.html", context)

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Wellcome"
        return context
    

class ProductsListView(ListView):
    model = Product
    template_name = "products.html"


    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        else:
            queryset
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["categories"] = category = ProductCategory.objects.all()
        return context


# def pruducts(request, category_id=None, page=1):
#     if category_id:
#         product = Product.objects.filter(category_id=category_id)
#     else:
#         product = Product.objects.all()
    
#     category = ProductCategory.objects.all()
#     per_page = 3
#     paginator = Paginator(product, per_page)
#     paginated_products = paginator.page(page)
#     context =  {
#         "products": paginated_products,
#         "categories": category,
#         }
    
#     return render(request, "products.html", context)

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
