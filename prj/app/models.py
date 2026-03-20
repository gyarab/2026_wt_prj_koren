from django.db import models

# Create your models here.
from django.db import models


class Znacka(models.Model):
    nazev = models.CharField(max_length=100)

    def __str__(self):
        return self.nazev


class Model(models.Model):
    nazev = models.CharField(max_length=100)
    znacka = models.ForeignKey(Znacka, on_delete=models.CASCADE, related_name="modely")

    def __str__(self):
        return self.nazev


class Auto(models.Model):
    nazev = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="auta")

    def __str__(self):
        return self.nazev


class Motorizace(models.Model):
    typ = models.CharField(max_length=100)
    vykon = models.IntegerField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name="motorizace")

    def __str__(self):
        return f"{self.typ} ({self.vykon} kW)"


class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.jmeno


class Recenze(models.Model):
    text = models.TextField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name="recenze")

    def __str__(self):
        return f"Recenze na {self.auto}"


class Komentar(models.Model):
    text = models.TextField()
    recenze = models.ForeignKey(Recenze, on_delete=models.CASCADE, related_name="komentare")

    def __str__(self):
        return f"Komentář k recenzi {self.recenze.id}"


class Hodnoceni(models.Model):
    hodnota = models.IntegerField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name="hodnoceni")
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE, related_name="hodnoceni")

    def __str__(self):
        return f"{self.hodnota} - {self.auto}"
