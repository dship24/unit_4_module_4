from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    is_favorite = models.BooleanField()
    
    
def create_contact(name, email, phone, is_favorite):
    new_contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    new_contact.save()
    return new_contact

def all_contacts():
    return Contact.objects.all()
    
def find_contact_by_name(name):
    try:
       return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None

def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, email):
    contact = find_contact_by_name(name)
    contact.email = email
    contact.save()

def delete_contact(name):
    contact = find_contact_by_name(name)
    contact.delete()