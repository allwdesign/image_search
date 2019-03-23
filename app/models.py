from django.db import models
from PIL import Image


class Photo(models.Model):
    image = models.ImageField(default='default.png', upload_to='uploaded_pics')

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
