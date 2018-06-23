#from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class Trench_99_528(models.Model):
    gid = models.AutoField(primary_key=True)
    contextkey = models.CharField(primary_key=True, max_length=20)
    type = models.CharField(max_length=50)
    shape_leng = models.IntegerField()
    shape_area = models.IntegerField()
    phase = models.IntegerField()
    geom = models.MultiPolygonField()

    class Meta:
        #unique_together = (("area_easting", "area_northing", "context_number"))
        db_table = 'excavation\".\"gis_99_526_polygon'
        managed = False
        #ordering = ["container_name"]
        verbose_name_plural = "Trench 99 526"
