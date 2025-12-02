from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home_view(request):
    return render(request, "home.html")


def hub_view(request):
    return render(request, "hub.html")

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # 1. Extract data from the validated form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['betreff']  # Use form field name
            message = form.cleaned_data['notiz']  # Use form field name

            # 2. Construct the email details
            recipient_email = 'info@pfadibrig.ch'

            # The email subject for the recipient
            email_subject = f"Neue Kontaktanfrage: {subject}"

            # The full body of the email
            email_body = f"""
            Name: {first_name} {last_name}
            Betreff: {subject}
            Nachricht:
            {message}
            """

            # 3. Send the email!
            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,  # Sender's email from settings
                    [recipient_email],  # List of recipients
                    fail_silently=False,
                )

                # Success message (optional)
                return render(request, 'contact_success.html')  # Redirect to a success page

            except Exception as e:
                # Error handling (e.g., logging or showing an error message)
                print(f"Error sending email: {e}")
                return render(request, 'contact_failed.html', {'form': form, 'error_message': 'Failed to send email.'})

    else:
        # For a GET request, create a blank form
        form = ContactForm()

    return render(request, 'contact_success.html')
