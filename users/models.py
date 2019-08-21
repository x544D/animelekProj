from django.db import models

# users model
class Members(models.Model):
  # id is already by default made set to auto increased by python
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20, blank=True)

