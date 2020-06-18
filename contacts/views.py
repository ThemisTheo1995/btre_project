from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.template import loader

#Contact form toRent
def rent_contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    #hidden
    realtor_email = request.POST['realtor_email']
    realtor_name = request.POST['realtor_name']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/rent/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    #Email Send
    html_message = loader.render_to_string(
       'realtor_email/rent_inquiry.html',
       {
        'name':name,
        'listing':listing,
        'phone':phone,
        'email':email,
        'realtor_email':realtor_email,
        'realtor_name':realtor_name,
        'message':message,
        'listing_id':listing_id,
        }
        )  
    send_mail(
       'Property Listing Inquiry',
       '',
       'themisstheodoratos@gmail.com',
       [realtor_email, 'themistheodoratos@gmail.com'],
       fail_silently=False,
       html_message=html_message
     )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/rent/'+listing_id)

#Contact form forSale
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    #hidden
    realtor_email = request.POST['realtor_email']
    realtor_name = request.POST['realtor_name']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    #Email Send
    html_message = loader.render_to_string(
       'realtor_email/rent_inquiry.html',
       {
        'name':name,
        'listing':listing,
        'phone':phone,
        'email':email,
        'realtor_email':realtor_email,
        'realtor_name':realtor_name,
        'message':message,
        'listing_id':listing_id,
        }
        )  
    send_mail(
       'Property Listing Inquiry',
       '',
       'themisstheodoratos@gmail.com',
       [realtor_email, 'themistheodoratos@gmail.com'],
       fail_silently=False,
       html_message=html_message
     )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)