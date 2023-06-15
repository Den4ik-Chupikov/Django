from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    #post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    topic = models.ManyToManyField(Topic, related_name= 'topic')
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='post', )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Like(models.Model):
    pass