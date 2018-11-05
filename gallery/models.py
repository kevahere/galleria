from django.db import models

# Create your models here.
class Location(models.Model):
    """Class that defines the image location"""
    location = models.CharField(max_length= 30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    """class defining the photo category"""
    category = models.CharField(max_length= 30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    @classmethod
    def search_category(cls,search_term):
        #returns a searched image by category
        return cls.objects.filter(category_contains=search_term)

class Images(models.Model):
    """class that defines the images"""

    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now= True)
    location = models.ForeignKey(Location,default=1)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save_pictures(self):
        self.save()

    @classmethod
    def delete_pictures(cls,id):
        #deletes the pictures from the database
        pic = cls.objects.filter(id = id)
        pic.delete()


    @classmethod
    def get_pic_by_id(cls,id):
        #gets a specific picture by id
        return cls.objects.filter(id=id)

    @classmethod
    #to find image by location
    def filter_by_location(cls,location):
        return cls.objects.filter(location=location)

    @classmethod
    #to find image by category
    def filter_by_category(cls,category):
        return cls.objects.filter(category=category)

    @classmethod
    def all_pics(cls):
    #gets all the pictures
        return cls.objects.all().order_by('-id')






