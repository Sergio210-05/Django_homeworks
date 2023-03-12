from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    image = models.ImageField(null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, image: {self.image}, ' \
               f'release_date: {self.release_date}, lte_exists:{self.lte_exists}, slug: {self.slug}'
