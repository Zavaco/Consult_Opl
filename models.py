from django.db import models


class Navbar(models.Model):
      home = models.TextField()
      about = models.TextField()
      services = models.TextField()
      portfolio = models.TextField()
      blog = models.TextField()
      contact = models.CharField(max_length=100, null=True)

      def __str__(self):
          return f'{self.pk}'



#
#
class Teacher(models.Model):
     name = models.CharField(max_length=50)
     subject = models.CharField(max_length=50)
     course_id=models.CharField(max_length=50)



