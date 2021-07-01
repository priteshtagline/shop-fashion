from django.http import JsonResponse
from django.views import View


class LikeProductView(View):
    def post(self, request):
        if not self.request.user.is_authenticated:
            return JsonResponse({'status': False, 'message': 'login_required'}, status=200)
        user = self.request.user
        get_request = request.POST.get
        try:
            if get_request('like_action') == 'add':
                user.like_product.add(get_request('product_id'))
                return JsonResponse({'status': True, 'message': 'Product add in like list'}, status=200)
            else:
                user.like_product.remove(get_request('product_id'))
                return JsonResponse({'status': True, 'message': 'Product remove for like list'}, status=200)
        except:
            return JsonResponse({'status': False, 'message': 'Product not found.'}, status=200)
