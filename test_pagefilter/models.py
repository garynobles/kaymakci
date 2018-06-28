from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    #store_id = models.ForeignKey(Store, db_column='store_id', on_delete = models.PROTECT)
    location_id = models.AutoField(primary_key=True)
    location_identifier = models.IntegerField(blank=True, null=True)

    location_type = models.CharField(max_length=100, blank=True, null=True)
    current_location_tmp = models.CharField(max_length=100, blank=True, null=True)
    location_name = models.CharField(max_length=100, blank=True, null=True)
    #icon_desc = models.ForeignKey(Icon, db_column='icon_desc', on_delete = models.PROTECT, null=True, blank=True)

    orderby = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.location_name

    class Meta():
        managed=False
        db_table = 'samples\".\"location'
        #ordering = ["orderby"]
        #verbose_name_plural = "locations"
