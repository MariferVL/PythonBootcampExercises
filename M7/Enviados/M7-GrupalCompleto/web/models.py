from django.db import models

from django.utils import timezone

# Create your models here.
class Funfact(models.Model):
  idm = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=1000)
  photo = models.ImageField(
    upload_to='media/photo_funfacts',
    default='media/default/default.jpg',
    blank=True)

class Scale(models.Model):
  idm = models.CharField(max_length=100)
  photo = models.ImageField(
    upload_to='media/photo_scale',
    default='media/default/default.jpg',
    blank=True)
  typesb = models.CharField(max_length=100)
  text = models.CharField(max_length=100)
  cause = models.CharField(max_length=100)

class Tip(models.Model):
  ICONS= (
    ('fa-solid fa-droplet','agua'),
    ('fa-solid fa-wheat-awn','comida'),
    ('fa-solid fa-person-running','deporte'),
    ('fa-solid fa-comment-medical','medicamento'),
    ('fa-solid fa-comment','otros'),
  )
  idm = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=100)
  icon = models.CharField(max_length=100, choices=ICONS)

class Post(models.Model):
  idm = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=100)
  photo = models.ImageField(
    upload_to='media/photo_posts',
    default='media/default/default.jpg',
    blank=True)

class Link(models.Model):
  ICONS= (
    ('fa-solid fa-globe','web'),
    ('fa-solid fa-house-medical','salud'),
    ('fa-solid fa-link','otros'),
  )
  idm = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=100)
  icon = models.CharField(max_length=100, choices=ICONS)



class Photo(models.Model):
  idm = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=1000)
  photo = models.ImageField(
    upload_to='media/photo_gallery',
    default='media/default/default.jpg',
    blank=True)



class Suscriptor(models.Model):
  full_name = models.CharField(max_length=100)
  email = models.CharField(max_length=1000)



class Caca(models.Model):
  tipo = models.CharField(max_length=100)







# -----------------------------------------
class Contact(models.Model): 
  name = models.CharField(max_length=200)
  sender = models.EmailField()
  subject = models.CharField(max_length=200)
  message = models.TextField()
  cc_myself = models.BooleanField(default=False)
  sending_date = models.DateTimeField(blank=True, null=True)

  def sent(self):
    self.sending_date = timezone.now()
    self.save()

  def str(self):
    return self.sender

