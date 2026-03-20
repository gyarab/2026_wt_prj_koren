from django.db import models

# Create your models here.
from django.db import models


from django.db import models


class Znacka(models.Model):
    nazev = models.CharField(max_length=100)


class Model(models.Model):
    nazev = models.CharField(max_length=100)
    znacka = models.ForeignKey(Znacka, on_delete=models.CASCADE)


class Auto(models.Model):
    nazev = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)


class Motorizace(models.Model):
    typ = models.CharField(max_length=100)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)


class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100)


class Recenze(models.Model):
    text = models.TextField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)


class Komentar(models.Model):
    text = models.TextField()
    recenze = models.ForeignKey(Recenze, on_delete=models.CASCADE)


class Hodnoceni(models.Model):
    hodnota = models.IntegerField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE)
