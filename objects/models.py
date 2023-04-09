from django.db import models


class ObjectTable(models.Model):
    address = models.TextField(blank=False)
    administrate_county = models.CharField(max_length=6, blank=False)
    cod_number = models.CharField(max_length=16, blank=True)
    ind_zone = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    area = models.CharField(max_length=100)
    comments = models.TextField()
    rev_count = models.IntegerField()
    type_obj = models.CharField(max_length=30)
    state_obj = models.CharField(max_length=100)
    sqr = models.IntegerField()
    own = models.CharField(max_length=100)
    actual_user = models.CharField(max_length=100)
    n_prot = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    check_company = models.CharField(max_length=100)
    law = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', default='')

# class ObjectImage(models.Model):
#     obj = models.ForeignKey(ObjectTable, on_delete=models.PROTECT, related_name='object_image')
#     photo = models.ImageField(blank=False, upload_to='photos/%Y/%m/%d/')

#
# class ObjectVideo(models.Model):
#     obj = models.ForeignKey(ObjectTable, on_delete=models.PROTECT, related_name='object_video')
#     video = models.FileField(blank=False, upload_to=f'video/%Y/%m/%d/')
