from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __iter__(self):
        # Example implementation, depending on your use case.
        yield from {
            "id": self.id,
            "name": self.name
        }.items()

    def __str__(self):
        return self.name
