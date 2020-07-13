from django.db import models
from SkewCorrector.lib.skewCorrector import Correction

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='media/')
    A = Correction(cover)
    postSkew = A.skewFix(cover)

    def __unicode__(self):
        return self.title

