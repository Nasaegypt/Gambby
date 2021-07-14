from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

SERVICE_TYPE = (
    ('At Home', 'At Home'),
    ('In Place', 'In Place'),
    ('Online', 'Online')
)
AVAILABILITY = (
    ('Active', 'Active'),
    ('Not Active', 'Not Active')
)
COST = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High')
)


def image_upload(instance, filename):
    imagename, extention = filename.split(".")
    return "services/%s.%s" % (instance.id, extention)


class Service(models.Model):  # table
    title = models.CharField(max_length=100)  # column
    # location
    service_type = models.CharField(max_length=15, choices=SERVICE_TYPE)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    availability = models.CharField(max_length=10, choices=AVAILABILITY)
    cost = models.CharField(max_length=10, choices=COST)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(70, 70)], format='JPEG',
                                     options={'quality': 60})

    slug = models.SlugField(blank=True, null=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.id) + "-" + self.title, allow_unicode=True)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
