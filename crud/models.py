from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=200)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def name_print(self):
        return self.name
