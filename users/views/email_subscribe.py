from django.http import JsonResponse
from django.views import View
from users.models import EmailSubscribe


class EmailSubscribeView(View):
    def post(self, request):
        subscribe, created = EmailSubscribe.objects.get_or_create(
            email=request.POST.get('email_subscribe'))
        message = "Successfully your email subscribed." if created else 'Your email allreday subscribed.'
        return JsonResponse({"status": True, "message": message}, status=200)
