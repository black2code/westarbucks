from django.db import models

class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'drinks'

class Category(models.Model):
    name = models.CharField(max_length=30)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Menu(models.Model):

    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'menus'


class Allergy(models.Model):
    allergy_name = models.CharField(max_length=30)
    name = models.ManyToManyField('Drink', through='Allergy_drink')


    class Meta:
        db_table = 'allergys'

class Allergy_drink(models.Model):

    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drinks'


class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)


    class Meta:
        db_table = 'nutritions'


class Image(models.Model):

    image_url = models.URLField(max_length=1000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name = models.CharField(max_length=30)
    size_ml = models.CharField(max_length=30)
    size_fluid_ounce = models.CharField(max_length=30)

    class Meta:
        db_table = 'sizes'


# Create your models here.
