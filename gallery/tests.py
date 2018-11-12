import datetime as dt
from django.test import TestCase
from .models import Editor,Image,tags



#Tests for Images
class ImageTestClass(TestCase):
    def setUp(self):

        #Creating a new tag and saving it
        self.new_tag = tags(name ='testing')
        self.new_tag.save()

        #Creating a new Image and saving it
        self.new_Image=Image(name ='TestImage', image = 'images/TestImage.jpg', pub_date = dt.time(), location = 'Nairobi', category = 'Fun' )
        self.new_Image.save()
        self.new_Image.tags.add(self.new_tag)

    def tearDown(self):
        category.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()

   