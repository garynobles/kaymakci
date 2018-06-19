from django.db import models

# Create your models here.


#class Contexts_spatial(models.Model):
#    area_easting = models.OneToOneField(area_easting,on_delete=models.RESTRICT,primary_key=True)
#    area_northing = models.OneToOneField(Area_northing,on_delete=models.RESTRICT,primary_key=True)
#    context_number = models.OneToOneField(Context_number,on_delete=models.RESTRICT,primary_key=True)

#    class Meta:
#        unique_together = (("area_easting", "area_northing", "context_number"))
#        db_table = 'excavation\".\"contexts_spatial'
        #ordering = ["container_name"]
        #verbose_name_plural = "containers"

class Context(models.Model):
    context_id  = models.AutoField(primary_key=True)
    area_easting = models.IntegerField(null=True)
    area_northing = models.IntegerField(null=True)
    context_number = models.IntegerField(null=True)
    context_type = models.CharField(max_length=100, blank=True, null=False)
    description = models.TextField( blank=True, null=True)
    deposition_interpretation = models.CharField(max_length=500, blank=True, null=True)
    subtable = models.CharField(max_length=25, blank=True, null=True)
    chronology = models.CharField(max_length=100, blank=True, null=True)
    chronology_source = models.CharField(max_length=100, blank=True, null=True)
    stratigraphic_narrative = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        unique_together = (("area_easting", "area_northing", "context_number"))
        db_table = 'excavation\".\"contexts'
        managed = False
        #ordering = ["container_name"]
        #verbose_name_plural = "containers"

        #REFERENCES options.context_type (context_type) MATCH FULL
        #REFERENCES options.context_chronology (chronology) MATCH FULL
        #REFERENCES options.context_chronology_source (chronology_source) MATCH FULL
        #REFERENCES sde.excavation_areas (area_northing, area_easting) MATCH SIMPLE
        #REFERENCES options.context_subtables (subtables) MATCH FULL
        #CONSTRAINT contexts_context_number_check CHECK (context_number > 0 AND context_number < 10000)
