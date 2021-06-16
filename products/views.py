from django.shortcuts import render
from django.http import HttpResponse
import json
from products.models.category import Category
from products.models.product import Product
from products.models.sub_category import SubCategory


def get_category_by_department(request):
    """Given department id by return category list

    Args:
        request ([get]): [get the department id]

    Returns:
        [json]: [category id, name json list]
    """
    department_id = request.GET.get('id', '')
    result = list(Category.objects.filter(
        department_id=department_id).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_subcategory_by_category(request):
    """Given category id by return sub category list

    Args:
        request ([get]): [get the category id]

    Returns:
        [json]: [sub category id, name json list]
    """
    category_id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=category_id).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_products_by_product(request):
    """Given product id by return product list exclude product for given id

    Args:
        request ([get]): [get the category id]

    Returns:
        [json]: [product id, name json list]
    """
    product_id = request.GET.get('id', '')
    result = list(Product.objects.exclude(id=product_id).values('id', 'title'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_products_by_department(request):
    """Given department id by return product list

    Args:
        request ([get]): [get the department id]

    Returns:
        [json]: [product id, name json list]
    """
    department_id = request.GET.get('id', '')
    result = list(Product.objects.filter(
        department_id=department_id).values('id', 'title', 'category__name', 'subcategory__name').order_by('category__name', 'subcategory__name', 'title'))
    return HttpResponse(json.dumps(result), content_type="application/json")
