from django.db import models

class Users(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    gender = models.CharField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id}.{self.first_name} - {self.last_name}"
    

