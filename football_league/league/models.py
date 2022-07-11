from django.db import models

class Liga(models.Model):
    nazwa = models.CharField(max_length=30)
    ilosc_klubow = models.CharField(max_length=30)
    prezes = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Klub(models.Model):
    nazwa = models.CharField(max_length=30)
    zalozyciel = models.CharField(max_length=50)
    prezes = models.CharField(max_length=50)
    data_zalozenia = models.DateField()
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nazwa



class Trener(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    wiek = models.CharField(max_length=3)
    klub = models.ForeignKey(Klub, on_delete=models.CASCADE)

    def __str__(self):
        return str( str(self.imie) + " " + str(self.nazwisko))

class Pilkarz(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    data_urodzenia = models.DateField()
    poprzedni_klub = models.CharField(max_length=100)
    numer_koszulki = models.CharField(max_length=3)
    klub = models.ForeignKey(Klub, on_delete=models.CASCADE)

    def __str__(self):
        return str( str(self.imie) + " " + str(self.nazwisko))

class Sedzia(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return str( str(self.imie) + " " + str(self.nazwisko))

class Adres(models.Model):
    miasto = models.CharField(max_length=20)
    ulica = models.CharField(max_length=20)
    numer_ulicy = models.CharField(max_length=5)
    def __str__(self):
        return str( str(self.miasto) + "," + str(self.ulica) + " " + str(self.numer_ulicy))

class Stadion(models.Model):
    nazwa = models.CharField(max_length=30)
    ilosc_miejsc = models.CharField(max_length=8)
    adres = models.ForeignKey(Adres, on_delete=models.CASCADE)
    klub = models.ForeignKey(Klub, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

class Mecz(models.Model):
    godzina_rozpoczecia = models.DateTimeField()
    wynik = models.CharField(max_length=6)
    gospodarz = models.ForeignKey(Klub, on_delete=models.CASCADE, related_name='klub1')
    gosc = models.ForeignKey(Klub, on_delete=models.CASCADE, related_name='klub2')
    sedzia = models.ForeignKey(Sedzia, on_delete=models.CASCADE)
    def __str__(self):
        return str( str(self.gospodarz) + " " + str(self.gosc))