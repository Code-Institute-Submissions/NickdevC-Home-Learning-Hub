from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Custom choices
APPOINTMENT_TIMES = (
    ('0', '15:00 - 15:15'),
    ('1', '15:15 - 15:30'),
    ('2', '15:30 - 15:45'),
    ('3', '15:45 - 16:00'),
    ('4', '16:00 - 16:15'),
    ('5', '16:15 - 16:30'),
    ('6', '16:30 - 16:45'),
)

TEACHERS = (
    ('0', 'Mr Oakley'),
    ('1', 'Mrs Brundle'),
    ('2', 'Mr Simons'),
    ('3', 'Miss Baxter'),
    ('4', 'Mrs Shepard'),
    ('5', 'Miss Edwards'),
)


# Date validator to stop past dates being selected
def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


# Appointments class for users to book an appointment slot
class Appointment(models.Model):
    parent_name = models.CharField(max_length=80)
    child_name = models.CharField(max_length=80)
    teacher_name = models.CharField(
        max_length=80, choices=TEACHERS, default='0')
    date = models.DateField(validators=[validate_date])
    time = models.CharField(
        max_length=50, choices=APPOINTMENT_TIMES, default='0')
    comment = models.TextField(default=None)

    class Meta:
        unique_together = ["teacher_name", "date", "time"]

    def __str__(self):
        return f"{self.date} | {self.parent_name} | {self.child_name}"
