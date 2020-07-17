from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = int(request.POST['user_id'])
    realtor_email = request.POST['realtor_email']

    #Check Login User submit a Rquest already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, "You already made an inquery for this listings")
        return redirect('/listings/'+listing_id)


    contact = Contact.objects.create(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

    send_mail(
      'Property listing Inquery',
      'There has been an inquer for ' + listing + '. Sign Admin Panel',
      'ashkanbeeu@gmail.com',
      [realtor_email, 'fazeli.esmaeel@gmail.com'],
      fail_silently=False
    )


    messages.success(request, 'Your request has been submited, the realtor will contact you soon.')

    return redirect('/listings/'+listing_id)
  

