from django.db import models

# Create your models here.
class Musician(models.Model):
    #id = models.AutoField(Primary_Key=True)
    first_name = models.CharField(max_length = 50, null = True)
    last_name = models.CharField(max_length = 50, blank = True)
    instruments = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    #id = models.AutoField(Primary_Key=True)
    artist = models.ForeignKey(Musician, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    release_date = models.DateField()

    rating = (
    (1, 'worst'),
    (2, 'bad'),
    (3,'not bad'),
    (4, 'good'),
    (5, 'excellent'),
    )
    num_stars = models.IntegerField(choices = rating)


    def __str__(self):
        return self.name + " ,Rating:" + str(self.num_stars)
