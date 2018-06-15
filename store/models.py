from django.db import models

# Create your models here.
class Store(models.Model):

    #id = models.IntegerField(default=0)
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=200, default='')
    address_1 = models.CharField(max_length=200, default='')
    address_2 = models.CharField(max_length=200, default='')
    region = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    zip = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default="Turkey")
    #user = models.CharField(max_length=200, default="Gygaia")
    #datestamp = models.DateTimeField(auto_now=True)

    #def __unicode__(self):
        #return self.store_id

    #def __str__(self):
        #return self.store_name

    class Meta():
        managed=False
        db_table = 'samples\".\"store'
        #ordering = ["store_name"]
        verbose_name_plural = "stores"
