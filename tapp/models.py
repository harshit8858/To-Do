from django.db import models

completed = (
    (True, "Completed"),
    (False, "Not Completed"),
)

class todo(models.Model):
    date = models.DateField()    # yyyy-mm-dd
    time = models.TimeField()
    label = models.CharField(max_length=40)
    now = models.DateTimeField(auto_now=True)
    check = models.BooleanField(choices = completed, default=False)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['date','time']