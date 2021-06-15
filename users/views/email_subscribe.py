from django.http import JsonResponse
from django.views import View
from users.models import EmailSubscribe


class EmailSubscribeView(View):
    def post(self, request):
        EmailSubscribe.objects.create(
            email=request.POST.get('email_subscribe'))
        return JsonResponse({"status": True}, status=200)
