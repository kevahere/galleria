from django.db import models

# Create your models here.
class Images(models.Model):
    """class that defines the images"""

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now= True)
    location = models.ForeignKey(Location,default=1)
    category = models.ManyToManyField(Category)

    class meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save_pictures(self):
        self.save()

    @classmethod
    def delete_pictures(cls,id):
        pic = cls.objects.filter(id = id)
        pic.delete