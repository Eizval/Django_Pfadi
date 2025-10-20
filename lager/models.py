from django.db import models
from django.conf import settings  # <-- import settings for custom user model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Kategorie")
    description = models.TextField(blank=True, null=True, verbose_name="Beschreibung")
    size = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name="Größe",
        help_text="Optional: Größenangabe für Artikel wie T-Shirts oder Schuhe"
    )

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', verbose_name="Kategorie")
    description = models.TextField(blank=True, null=True, verbose_name="Beschreibung")
    sku = models.CharField(max_length=50, unique=True, verbose_name="Artikelnummer")
    unit = models.CharField(max_length=50, default='Stück', verbose_name="Einheit")

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
