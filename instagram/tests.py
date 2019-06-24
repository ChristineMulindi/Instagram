from django.test import TestCase
from .models import Comment,Profile,Image
from django.contrib.auth.models import User

class InstagramTestClass(TestCase):
    def setUp(self):
        self.user= User(id=1,username='Christine',email='mulindichristine@gmail.com',password='1234')
        self.user.save()
        self.profile = Profile(bio='christine is awesome',profile_path='image/christine.jpg')
        self.profile.save()
        self.new_image = Image(id=1,caption='crazy chick', editor='Christine',image_path='image/christine-3134828_1920.jpg')
        self.new_image.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)
   
    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.editor,'Christine')

    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('Christine','Mulindi')
        fetched = Image.objects.get(editor='Mulindi')
        self.assertEqual(fetched.editor,'Mulindi')

    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    def test_search_by_username(self):
        self.profile.save_profile()        
        fetch_set = Profile.objects.get(user=1)
        self.assertTrue(fetch_set.id==1)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(editor='Christine')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)
