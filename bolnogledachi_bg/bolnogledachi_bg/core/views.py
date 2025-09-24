from django.shortcuts import render

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
# from ratelimit.decorators import ratelimit
import bleach
from .forms import ContactForm
from django.contrib import messages


def home(request):
    return render(
        request,
        'core/home.html',
        )
    
    
# def contact_form(request):
#     return render(
#         request,
#         'core/contact_form.html',
#         )
    
    
# ограничение: 5 заявки на минута на IP (адаптирай)
# @ratelimit(key='ip', rate='5/m', block=True)
def contact_view(request):
    """
    Показва и обработва контактната форма.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # взимаме чистите данни
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            service = form.cleaned_data['service']
            # sanitize message -> позволяваме само текст, без html
            raw_message = form.cleaned_data['message']
            message_clean = bleach.clean(raw_message, tags=[], strip=True)

            # Prepare email content (без чувствителни данни)
            subject = f"Нов контакт от {name} - {service}"
            body = (
                f"Име: {name}\n"
                f"Email: {email}\n"
                f"Телефон: {phone}\n"
                f"Услуга: {service}\n\n"
                f"Съобщение:\n{message_clean}"
            )

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # логни евентуално / покажи обща грешка
                messages.error(request, "Възникна проблем при изпращането. Моля опитайте по-късно.")
                # можеш да логнеш e за debugging
                return render(request, 'core/contact_success.html', {'sent': False})

            messages.success(request, "Благодарим! Вашето съобщение е изпратено.")
            return redirect('contact_form')  # или 'home' и т.н.
        else:
            # form невалиден
            messages.error(request, "Моля коригирайте грешките в формата.")
    else:
        form = ContactForm()

    return render(request, 'core/contact_form.html', {'form': form})
    

def about_us(request):
    return render(
        request,
        'core/about_us.html',
        )