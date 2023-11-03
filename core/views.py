from django.shortcuts import render
from django.core.mail import send_mail as sm
from django.core.mail import BadHeaderError
from django.contrib import messages

# Create your views here.
def indexPage(request):
    if(request.method == 'POST'):
        try:
            res = sm(
            subject = request.POST['subject'],
            message = request.POST['message'],
            from_email = 'shrinivasbbaldawa@gmail.com',
            recipient_list = ['shrinivasbbaldawa@gmail.com'],
            fail_silently=False,
            )
            messages.success(request, 'Message Sent!')
        except BadHeaderError:
            return messages.error("Invalid Header")
        
    return render(request, 'index.html')