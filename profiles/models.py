from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Level(models.Model):
    class LevelChoices(models.TextChoices):
        WOLF = "Wolf", "Wolf"
        PFADI = "Pfadi", "Pfadi"
        FENNER = "Fenner", "Fenner"
        WOLF_LEITER = "Wolf-Leiter", "Wolf-Leiter"
        PFADI_LEITER = "Pfadi-Leiter", "Pfadi-Leiter"

    class SecondLevelChoices(models.TextChoices):
        JUNG_PFADI = "Jung-Pfadi", "Jung-Pfadi"
        PFADI = "Pfadi", "Pfadi"
        OP = "OP", "OP"

    level = models.CharField(max_length=20, choices=LevelChoices.choices)
    second_level = models.CharField(
        max_length=20,
        choices=SecondLevelChoices.choices,
        null=True,
        blank=True,
    )

    def clean(self):
        super().clean()
        # second_level only applies when level = "Pfadi"
        if self.level == self.LevelChoices.PFADI:
            return
        if self.second_level:
            raise ValidationError({
                "second_level": "second_level is only allowed when level is 'Pfadi'."
            })

    def __str__(self):
        if self.level == self.LevelChoices.PFADI and self.second_level:
            return f"{self.level} - {self.second_level}"
        return self.level


class Profile(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    pfadi_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    level = models.ForeignKey('Level', on_delete=models.PROTECT, related_name='profiles')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    img = models.URLField(null=True, blank=True)
    visible = models.BooleanField(default=False)
    documents = models.JSONField(default=list, blank=True)

    def full_name(self):
        parts = [self.name]
        if self.second_name:
            parts.append(self.second_name)
        parts.append(self.last_name)
        return " ".join([p for p in parts if p])

    def __str__(self):
        return self.full_name()
