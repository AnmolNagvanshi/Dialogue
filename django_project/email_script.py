from django.core.mail import EmailMessage
email = EmailMessage(subject='test-email', body='testing body', to=['anmol6251@gmail.com'])
email.send()