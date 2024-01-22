from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import FileExtensionValidator
from profilesettings.models import Profile

class Post(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    profile_pic = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_pfp')
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    caption = models.TextField()
    post_image = models.ImageField(upload_to='posted_pictures', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    likes = models.ManyToManyField(User, blank = True, related_name='likes')

    def __str__(self):
        return self.name.name
    
    class Meta:
        ordering = ['-published_date']


class Comment(models.Model):

    post_comment = models.ForeignKey(Post, related_name = 'post_comment' , on_delete = models.CASCADE, blank = True, null = True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
