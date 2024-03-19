from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image= models.ImageField(upload_to="post/")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.post}"
    
class Contact(models.Model):
    full_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    message = models.TextField()

    def __str__(self):
        return f" {self.full_name} -  {self.phone_number} " 
    
class Gallery(models.Model):
    gallery_image= models.ImageField(upload_to="gallery/")
    created_date = models.DateTimeField(auto_now_add= True)
    modified_date = models.DateTimeField(auto_now=True)

    