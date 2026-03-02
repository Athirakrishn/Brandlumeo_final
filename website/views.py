import urllib.parse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, HeroSection, ContactMessage


def home(request):
    context = {
        "services": Service.objects.all(),
        "hero": HeroSection.objects.first()
    }
    return render(request, "website/index.html", context)


def services_page(request):
    return render(request, "website/services.html")


def about_page(request):
    return render(request, "website/about.html")


def portfolio_page(request):
    return render(request, "website/portfolio.html")


def blog_page(request):
    return render(request, "website/blog.html")


def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        company = request.POST.get("company", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            # We still save it to the DB for admin tracking 
            ContactMessage.objects.create(
                name=name,
                email=email,
                company=company,
                message=message,
            )
            
            # Construct the email body
            mail_body = f"Name: {name}\nEmail: {email}\n"
            if company:
                mail_body += f"Company: {company}\n"
            mail_body += f"\nMessage:\n{message}"

            # Create the mailto link
            subject = urllib.parse.quote(f"New Contact Form Submission from {name}")
            body = urllib.parse.quote(mail_body)
            # The destination email handle where the info should be received
            target_email = "Info@brandlumeo.com"
            mailto_url = f"mailto:{target_email}?subject={subject}&body={body}"
            
            # Render thank you page and pass the mailto_url to be triggered by JS
            return render(request, "website/thank_you.html", {"mailto_url": mailto_url})

        messages.error(request, "Please fill out your name, email, and message.")

    return render(request, "website/contact.html")


def thank_you_page(request):
    return render(request, "website/thank_you.html")


def privacy_page(request):
    return render(request, "website/privacy.html")


def terms_page(request):
    return render(request, "website/terms.html")


def cookies_page(request):
    return render(request, "website/cookies.html")


def calicut(request):
    return redirect("/", permanent=True)


def seo_kerala(request):
    return redirect("/", permanent=True)


def seo_uae(request):
    return redirect("/", permanent=True)
