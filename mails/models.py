from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    service = models.CharField(max_length=100, blank=True, null=True)
    division = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Specify custom related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Specify custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user'
    )

class Mail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    MAIL_TYPE_CHOICES = [
        ('arrived', 'Arrived'),
        ('departed', 'Departed')
    ]

    MAIL_STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('processed', 'Processed'),
        ('pending', 'Pending')
    ]

    type = models.CharField(max_length=10, choices=MAIL_TYPE_CHOICES)
    date = models.DateField()
    objet = models.TextField()
    expéditeur = models.CharField(max_length=100)
    destinataire = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    date_traitement = models.DateField(null=True, blank=True)
    observations = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=20, choices=MAIL_STATUS_CHOICES)
    pieces_jointes = models.FileField(upload_to='pieces_jointes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    test = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.numero}"
