from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    # TODO: Добавьте требуемые поля
    # pass
