from django.db import models
from django.conf import settings  # <-- import settings for custom user model
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Beschreibung")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Artikelnummer")
    unit = models.CharField(max_length=50, default='Stück', verbose_name="Einheit", blank=True, null=True)
    quantity = models.IntegerField(default=1, verbose_name="Menge")
    size = models.CharField(max_length=10, verbose_name="Groesse", blank=True, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='stocks', verbose_name="Artikel")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Menge")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ort")

    def __str__(self):
        return f"{self.item.name} - {self.quantity} {self.item.unit}"

class Borrow(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Artikel")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <-- use AUTH_USER_MODEL instead of User
        on_delete=models.CASCADE,
        verbose_name="Benutzer"
    )
    quantity = models.PositiveIntegerField(verbose_name="Menge")
    borrowed_at = models.DateTimeField(auto_now_add=True, verbose_name="Ausleihdatum")
    returned_at = models.DateTimeField(blank=True, null=True, verbose_name="Rückgabedatum")

    STATUS_CHOICES = [
        ('borrowed', 'Ausgeliehen'),
        ('returned', 'Zurückgegeben'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed', verbose_name="Status")

    def __str__(self):
        return f"{self.quantity}x {self.item.name} an {self.user.username}"


class Sold(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="Artikel")
    email = models.EmailField(verbose_name="Benutzer-E-Mail")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Menge")
    sold_at = models.DateTimeField(default=timezone.now, verbose_name="Verkauft am")
    notes = models.TextField(blank=True, null=True, verbose_name="Bemerkungen")

    def __str__(self):
        return f"{self.quantity}x {self.item.name} an {self.email}"


# Pending items (waiting for approval)
class Pending(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ausstehend'),
        ('approved', 'Genehmigt'),
        ('rejected', 'Abgelehnt'),
        ('cancelled', 'Storniert'),
        ('sold', 'Verkauft'),
    ]

    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name="Artikel")
    email = models.EmailField(verbose_name="Benutzer-E-Mail")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Menge")
    request_date = models.DateTimeField(default=timezone.now, verbose_name="Anfrage-Datum")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    notes = models.TextField(blank=True, null=True, verbose_name="Bemerkungen")

    def __str__(self):
        return f"{self.quantity}x {self.item.name} an {self.email} [{self.status}]"

    def save(self, *args, **kwargs):
        # Automatically move approved items to Sold
        if self.status == 'approved':
            Sold.objects.create(
                item=self.item,
                email=self.email,
                quantity=self.quantity,
                notes=self.notes
            )
        super().save(*args, **kwargs)