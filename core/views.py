from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError
from django.contrib import messages

# Create your views here.
def indexPage(request):
    if(request.method == 'POST'):
        try:
            mymessage = EmailMultiAlternatives(
                subject=request.POST['subject'],
                body="This is a message from " + request.POST['name'] + " \n " + " \n " + request.POST['message'],
                to=['contactus@ahappyindustries.com'],
                from_email='contactus@ahappyindustries.com',
                reply_to=[request.POST['email']]
            )
            mymessage.send()
            messages.success(request, 'Message Sent!')
        except BadHeaderError:
            return messages.error("Invalid Header")
        
    return render(request, 'index.html')