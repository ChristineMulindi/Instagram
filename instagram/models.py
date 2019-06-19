from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, null=True)
    image_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    caption = models.CharField(max_length=220, default="")


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item

    @classmethod
    def get_image_by_id(cls,id):
        fetched_image = cls.objects.get(id=id)
        return fetched_image





        