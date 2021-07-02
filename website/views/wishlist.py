from django.http import JsonResponse
from django.views import View
from products.models.product import Product
from users.models import UserWihslistProduct, UserWishlist


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

                return JsonResponse({'status': True, 'message': 'Product add in wishlist'}, status=200)

            elif wish_list_type == 'remove':
                UserWihslistProduct.objects.get(
                    id=get_request('wishlist_record_id')).delete()
                return JsonResponse({'status': True, 'message': 'Product remove for wishlist'}, status=200)

            elif wish_list_type == 'remove_wishlist':
                UserWishlist.objects.get(
                    id=get_request('wishlist_id')).delete()
                return JsonResponse({'status': True, 'message': 'Remove wishlist'}, status=200)
                
            else:
                return JsonResponse({'status': False, 'message': 'Something went wrong.'}, status=200)
        except:
            return JsonResponse({'status': False, 'message': 'Product or wishlist not found.'}, status=200)
