from django.shortcuts import render
from django.http import HttpResponse
import json
from products.models.category import Category


def get_category_by_department(request):
    id = request.GET.get('id', '')
    result = list(Category.objects.filter(
        department_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
