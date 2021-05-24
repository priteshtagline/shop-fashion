from django.shortcuts import render
from django.http import HttpResponse
import json
from products.models.category import Category
from products.models.product import Product
from products.models.sub_category import SubCategory


def get_category_by_department(request):
    id = request.GET.get('id', '')
    result = list(Category.objects.filter(
        department_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_subcategory_by_category(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_products_by_product(request):
    id = request.GET.get('id', '')
    result = list(Product.objects.exclude(id=id).values('id', 'title'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_products_by_department(request):
    id = request.GET.get('id', '')
    result = list(Product.objects.filter(
        department_id=id).values('id', 'title'))
    return HttpResponse(json.dumps(result), content_type="application/json")
