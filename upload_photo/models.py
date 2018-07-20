# models.py
from django.db import models




# insert the photobatch_processing table, link with a foreign key
class Photobatch(models.Model):
    pb_id = models.AutoField(primary_key=True)
    photobatch_id = models.CharField(max_length=200, default='', blank=True, null=True)

    def __str__(self):
        return self.photobatch_id

    class Meta():
        managed=False
        db_table = 'excavation\".\"photobatch_processing'
        # ordering = ["container_name"]
        # verbose_name_plural = "containers"



#upload images
class Attachment(models.Model):
    file = models.FileField(upload_to='testing/tests')
    photobatch = models.IntegerField(blank=True, null=True)
    #photobatch = models.ForeignKey(Photobatch, db_column='photobatch_id', on_delete = models.DO_NOTHING)
    upload_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photobatch

    class Meta():
        managed=False
        db_table = 'excavation\".\"photobatch_photos'
        # ordering = ["container_name"]
        # verbose_name_plural = "containers"
