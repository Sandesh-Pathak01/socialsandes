from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import FileExtensionValidator
from home import models as postmodel

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(
        upload_to='profilepics',
        default='default.png',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    pid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, null=True, blank=True)
    name = models.CharField(max_length=50, default='Unknown User', blank=True)
    email = models.EmailField(max_length=50, default='', blank=True)
    dob = models.CharField(max_length=50, default='', blank=True)
    gender = models.CharField(max_length=50, default='', blank=True)
    bio = models.TextField(default='', blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def follow(self, user):
        self.followers.add(user)

    def unfollow(self, user):
        self.followers.remove(user)

    def is_following(self, user):
        return self.followers.filter(pk=user.pk).exists()

    def followers_count(self):
        return self.followers.count()
    
    def following_count(self):
        return self.user.following.count()

    def __str__(self):
        return self.name
    


