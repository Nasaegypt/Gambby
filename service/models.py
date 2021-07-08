from django.db import models

# Create your models here.

SERVICE_TYPE = (
    ('At Home', 'At Home'),
    ('In Place', 'In Place')
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


class Service(models.Model):  # table
    title = models.CharField(max_length=100)  # column
    # location
    service_type = models.CharField(max_length=15, choices=SERVICE_TYPE)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    availability = models.CharField(max_length=10, choices=AVAILABILITY)
    # category
    cost = models.CharField(max_length=10, choices=COST)

    def __str__(self):
        return (self.title)
