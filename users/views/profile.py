from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from users.forms.email_change import UserEmailChnageForm
from users.forms.password_change import UserPasswordChnageForm
from users.forms.personal_info_chnage import UserPersonalInfoChnageForm
from users.models import UserWishlist, UserWihslistProduct
from django.db.models import Count


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    """This view is for the user profile page which displays email, password and personal info chnage form.
    The view extend for TempletView django metohd then three form pass in single profile templet and render to html.
    Post method in check wiche form fill by user then perfome oprtaion and apropriate change to user profile data
    and send response.
    """
    login_url = 'user:login'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        kwargs['personal_info_change_form'] = UserPersonalInfoChnageForm(
            user, initial={'first_name': user.first_name, 'last_name': user.last_name})
        kwargs['password_change_form'] = UserPasswordChnageForm(user)
        kwargs['email_change_form'] = UserEmailChnageForm(user)
        user_wishlist = UserWishlist.objects.filter(user=user)
        kwargs['user_wishlist'] = user_wishlist.values(
            'name', 'id').annotate(product_count=Count('userwihslistproduct'))
        user_wishlist_ids = [wishlist.id for wishlist in user_wishlist]
        kwargs['user_wishlist_product'] = UserWihslistProduct.objects.filter(wishlist_id__in=user_wishlist_ids)
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        user = self.request.user
        if 'first_name' in form_data and 'last_name' in form_data:
            personal_info_change_form = UserPersonalInfoChnageForm(
                user, form_data)
            if personal_info_change_form.is_valid():
                personal_info_change_form.save()
            else:
                return JsonResponse({'status': False, 'errors': personal_info_change_form.errors}, status=200)

        elif 'new_password' in form_data and 'current_password' in form_data:
            password_change_form = UserPasswordChnageForm(user, form_data)
            if password_change_form.is_valid():
                password_change_form.save()
                update_session_auth_hash(request, user)
            else:
                return JsonResponse({'status': False, 'errors': password_change_form.errors}, status=200)

        else:
            email_change_form = UserEmailChnageForm(user, form_data)
            if email_change_form.is_valid():
                email_change_form.save()
            else:
                return JsonResponse({'status': False, 'errors': email_change_form.errors})

        return JsonResponse({"status": True, "errors": ""}, status=200)
