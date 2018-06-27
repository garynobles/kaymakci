#from django.db import models

# Create your models here.
#from django.contrib.gis.db import models
from django.db import models
from django.contrib.gis.db import models as gismodels

class WorldBorder(gismodels.Model):
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
    mpoly = gismodels.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

#unit_srid = 4326
unit_srid = 32635

#unit_srid_2 =
#GEOGCS["GCS_WGS_1984",
#    DATUM["D_WGS_1984",
#        SPHEROID["WGS_1984",6378137.0,298.257223563]],

#        PRIMEM["Greenwich",0.0],

#        UNIT["Degree",0.0174532925199433]],
#PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],
#PARAMETER["Central_Meridian",27.0],
#PARAMETER["Scale_Factor",0.9996],
#PARAMETER["Latitude_Of_Origin",0.0],
#UNIT["Meter",1.0]],VERTCS["WGS_1984",
#DATUM["D_WGS_1984",
#SPHEROID["WGS_1984",6378137.0,298.257223563]],
#PARAMETER["Vertical_Shift",0.0],
#PARAMETER["Direction",1.0],
#UNIT["Meter",1.0]]

class Trench_99_528(gismodels.Model):
    gid = models.AutoField(primary_key=True)
    #contextkey = models.CharField(primary_key=False, max_length=20)
    #type = models.CharField(max_length=50)
    #shape_leng = models.IntegerField()
    #shape_area = models.IntegerField()
    #phase = models.IntegerField()
    geom = gismodels.MultiPolygonField(srid=unit_srid)

    class Meta:
        #unique_together = (("area_easting", "area_northing", "context_number"))
        db_table = 'excavation\".\"gis_99_526_polygon'
        managed = False
        #ordering = ["container_name"]
        #verbose_name_plural = "Trench 99 526"

class Photobatch(gismodels.Model):
    id = models.AutoField(primary_key=True)
    #contextkey = models.CharField(primary_key=False, max_length=20)
    #type = models.CharField(max_length=50)
    #shape_leng = models.IntegerField()
    #shape_area = models.IntegerField()
    #phase = models.IntegerField()
    geom = gismodels.MultiPolygonField()

    class Meta:
        #unique_together = (("area_easting", "area_northing", "context_number"))
        db_table = 'excavation\".\"photobatch_processing'
        managed = False
        #ordering = ["container_name"]
        #verbose_name_plural = "Trench 99 526"
