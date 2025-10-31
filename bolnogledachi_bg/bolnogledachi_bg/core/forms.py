# core/forms.py
from django import forms
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Име и фамилия (задължително)',
            'class': 'input-field'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'E-mail (задължително)',
            'class': 'input-field'
        })
    )
    phone = forms.RegexField(
        regex=r'^(\+359|0)(?:8|9)[0-9]{7,8}$',
        error_messages={'invalid': 'Моля въведете валиден телефонен номер.'},
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Телефон (задължително)',
            'class': 'input-field'
        })
    )
    service = forms.ChoiceField(
        choices=[
            ('home', 'Болногледач почасово'),
            ('hospital', 'Болногледач на пълен работен ден'),
            ('247', 'Болногледач 24/7'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'input-field'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 8,
            'placeholder': 'Вашето съобщение (задължително)',
            'class': 'textarea-field'
        }),
        max_length=2000,
        required=True
    )

    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    # recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=False)

    def clean_honeypot(self):
        data = self.cleaned_data.get('honeypot')
        if data:
            raise forms.ValidationError("Spam detected.")
        return data


# # core/forms.py
# from django import forms
# # from captcha.fields import ReCaptchaField             # ако използваш django-recaptcha
# # from captcha.widgets import ReCaptchaV2Checkbox      # или V3 widget по избор

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.RegexField(
#         regex=r'^(\+359|0)(?:8|9)[0-9]{7,8}$',  # примерен бг формат - адаптирай ако искаш
#         error_messages={'invalid': 'Моля въведете валиден телефонен номер.'},
#         required=True
#     )
#     service = forms.ChoiceField(choices=[
#         ('home', 'Болногледач за дома'),
#         ('hospital', 'Болногледач за болница'),
#         ('247', 'Болногледач 24/7'),
#     ], required=True)
#     message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)

#     # Honeypot field (bots го попълват — ние ще го валидираме)
#     honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

#     # reCAPTCHA (използвай само ако имаш добавен django-recaptcha)
#     # recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=False)

#     def clean_honeypot(self):
#         data = self.cleaned_data.get('honeypot')
#         if data:
#             raise forms.ValidationError("Spam detected.")
#         return data