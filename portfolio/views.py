from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def contact_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)

def portfolio_home(request):
    return render(request, 'home.html')


def codewill_coming_soon(request):
    return render(request, 'codewill_coming_soon.html')



def custom_404(request, exception):
    return render(request, '404.html', status=404)


from .models import Project

def portfolio_home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'projects': projects})

def fake_admin(request):
    return render(request, 'sujkusu2812.html')