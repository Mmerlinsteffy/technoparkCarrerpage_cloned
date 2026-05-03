from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=90)
    closing_date=models.DateField()
    company=models.CharField(max_length=99)
    posted_on=models.DateField()
    address=models.TextField(blank=True)
    email=models.EmailField(blank=True)
    urlc=models.URLField(blank=True)
    class Meta:
        verbose_name_plural='Techpark'
    def __str__(self):
        return self.title