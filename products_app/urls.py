from django.urls import path

from .views import pruducts, add_to_basket, del_from_basket


urlpatterns = [
   path("", pruducts, name="products-page"),
   path("/category/<int:category_id>", pruducts, name="category"),
   path("/page/<int:page>", pruducts, name="paginator"),
   path("/baskets/add/<int:product_id>", add_to_basket, name="add_to_basket"),
   path("/baskets/remove/<int:bask_id>", del_from_basket, name="del_from_basket"),


]
