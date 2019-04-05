from django.db import models

class Event(models.Model):
    CATEGORY = (
        ('fire', 'Fire'),
        ('earth', 'Earth'),
        ('water', 'Water'),
        ('storm', 'Storm'),
        ('disease', 'Disease'),
        ('industrial', 'Industrial')
    )

    SEVERITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, default=None, blank=True)
    location = models.CharField(max_length=200)
    severity = models.CharField(max_length=10, choices=SEVERITY,
                                default='medium')
    category = models.CharField(max_length=10, choices=CATEGORY,
                                default='fire')

    def __str__(self):
        return "{} [{}] at {}".format(
            self.name, self.severity, self.location)


class PersonStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    other_name = models.CharField(max_length=200, blank=True)
    id_number = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField()
    added_by = models.ForeignKey('Person', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, default=None,
                              on_delete=models.CASCADE)
    status = models.ForeignKey(PersonStatus, null=True, default=None,
                               on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        string = self.first_name
        if self.last_name != '':
            string = "{}, {}".format(self.last_name, string)
        if self.other_name != '':
            string += " ({})".format(self.other_name)
        return string
