from django.http import JsonResponse
from django.views import View


class WishlistView(View):
    def post(self, request):
        if not self.request.user.is_authenticated:
            return JsonResponse({'status': False, 'message': 'login_required'}, status=200)
        user = self.request.user
        try:
            if request.POST.get('wishlist_type') == 'add':
                user.wishlist_product.add(request.POST.get('product_id'))
                return JsonResponse({'status': True, 'message': 'Product add in wish list'}, status=200)
            else:
                user.wishlist_product.remove(request.POST.get('product_id'))
                return JsonResponse({'status': True, 'message': 'Product remove for wish list'}, status=200)
        except:
            return JsonResponse({'status': False, 'message': 'Product not found.'}, status=200)
