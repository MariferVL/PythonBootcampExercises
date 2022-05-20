from pickle import TRUE
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here. ORM Object Relational Mapping


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

    def __str__(self):
        return self.name


class Presents(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    features = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200)
    guide_name = models.CharField(max_length=200)
    workshop_date = models.DateTimeField(blank=True, null=True)
    img_path = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'bp.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class SalesOrder(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    receiver_email = models.CharField(max_length=45, blank=True, null=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(
        'Salesorder', models.DO_NOTHING, blank=True, null=True)
    present = models.ForeignKey(
        'Presents', models.DO_NOTHING, blank=True, null=True)
