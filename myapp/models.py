from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    country_code = models.CharField(max_length=5)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country_code}{self.phone_number}"
