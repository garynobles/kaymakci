from django.db import models

# Create your models here.








#store
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

class Location(models.Model):
    store_id = models.ForeignKey(Store, db_column='store_id', on_delete = models.PROTECT)
    location_id = models.AutoField(primary_key=True)
    location_identifier = models.IntegerField(blank=True, null=True)
    #store_id = models.IntegerField(blank=True, null=True)
    location_type = models.CharField(max_length=100, blank=True, null=True)
    current_location_tmp = models.CharField(max_length=100, blank=True, null=True)
    location_name = models.CharField(max_length=100, blank=True, null=True)

    #ALTER TABLE samples."location" ADD CONSTRAINT fk_location_store FOREIGN KEY ( store_id ) REFERENCES samples.store( store_id );

    #def __unicode__(self):
        #return self.location_id

    def __str__(self):
        return self.location_name

    class Meta():
        managed=False
        db_table = 'samples\".\"location'
        ordering = ["location_name"]
        verbose_name_plural = "locations"
