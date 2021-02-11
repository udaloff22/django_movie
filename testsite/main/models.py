from django.db import models

# Create your models here.

class Categoty(models.Model):
    """Category"""

    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Actor(models.Model):
    """Actor"""

    name = models.CharField('Name', max_length=100)
    age = models.PositiveIntegerField('Age', default=0)
    models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and Directors'
        verbose_name_plural = 'Actors and Directors'
