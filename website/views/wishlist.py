from django.http import JsonResponse
from django.views import View
from users.models import UserWishlist
from users.models import UserWihslistProduct
from products.models.product import Product


class WishlistView(View):
    def post(self, request):
        if not self.request.user.is_authenticated:
            return JsonResponse({'status': False, 'message': 'login_required'}, status=200)
        try:
            user = self.request.user
            get_request = request.POST.get
            wish_list_type = get_request('wishlist_type')
            if wish_list_type == 'add':
                product_id = get_request('product_id')
                wishlist_name = get_request('wishlist_name').lower()
                wishlist, created = UserWishlist.objects.get_or_create(
                    user=user, name=wishlist_name)
                UserWihslistProduct.objects.get_or_create(
                    wishlist_id=wishlist.id, product_id=product_id)

                if get_request('remove_wishlist') == 'True':
                    default_wish_list, created = UserWishlist.objects.get_or_create(
                        user_id=user.id, name='wish list')
                    print(default_wish_list.id)
                    UserWihslistProduct.objects.get(
                        wishlist_id=default_wish_list.id, product_id=product_id).delete()

                return JsonResponse({'status': True, 'message': 'Product add in wish list'}, status=200)
            elif wish_list_type == 'remove':
                UserWihslistProduct.objects.get(id=2).delete()
                return JsonResponse({'status': True, 'message': 'Product remove for wish list'}, status=200)
            else:
                UserWishlist.objects.get(id=5).delete()
                return JsonResponse({'status': True, 'message': 'Delete wish list'}, status=200)
        except:
            return JsonResponse({'status': False, 'message': 'Product or wishlist not found.'}, status=200)
