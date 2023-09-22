from django.shortcuts import render
from .models import Image
from django.core.mail import EmailMessage
from django.db.models import DateTimeField
from django.db.models.functions import Trunc

# Create your views here.
def home(request):
    context = {}
    images = Image.objects.all()
    filtered = (x for x in images if x.isHighlight==True)
    print(images)
    context['images'] = filtered
    context['email_sent'] = 0

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_messsage = EmailMessage(
            subject = name + "||" + subject,
            body = message,
            to = ['rishitajayant@outlook.com'],
            headers = {"Reply-To": email}
        )

        sent = email_messsage.send()
        if(sent == 1):
            context['email_sent'] = 1
            
    return render(request, "index.html", context)

def ItemView(request):
    context = {}
    id=request.POST.get('id')
    image = Image.objects.get(id=id)
    context['image'] = image
    return render(request, "item-view.html", context)


def ShowAll(request):
    context = {}
    images = Image.objects.order_by('-id')
    context['images'] = images
    return render(request, "all-works.html", context)