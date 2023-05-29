from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    establishment = models.TextField(blank=True)
    foundername = models.TextField(blank=True)
    founderage = models.TextField(blank=True)
    foundereducation = models.TextField(blank=True)
    website = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.TextField(blank=True)
    equity = models.TextField(blank=True)
    patents_published = models.TextField(blank=True)
    cin_no = models.TextField(blank=True)
    incorporation_type = models.TextField(blank=True)

    startupname = models.TextField(blank=True)
    instagramurl = models.TextField(blank=True)
    department = models.TextField(blank=True)
    youtubeurl = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)   #
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    

# Job posting
class Jobpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)   #
    user = models.CharField(max_length=100)
    jobposition = models.TextField()
    joblocation = models.TextField()
    jobtime = models.TextField()
    jobsalary = models.TextField()
    jobabout = models.TextField()
    joblink = models.TextField()

    # jobcompany = models.TextField(max_length=255, default='My Company')
    jobcompany = models.TextField()
    # jobmodechoices = (
    #     ('office', 'Work From Office'),
    #     ('remote', 'Work From Home'),
    #     ('hybrid', 'Hybrid')
    # )
    # jobmode = models.CharField(max_length=20, default='Work From Office')
    jobmode = models.TextField()
    # jobexperiencechoices = (
    #     ('belowtwo', '0 to 2 years'),
    #     ('twotofive', '2 to 5 years'),
    #     ('fivetoten', '5 to 10 years'),
    #     ('aboveten', 'Above 10 years')
    # )
    # jobexperience = models.CharField(max_length=20, choices=jobexperiencechoices, default='0 to 2 years')
    jobexperience = models.TextField()
    jobdepartment = models.TextField(max_length=240, default='Engineering')
    # jobuploaddate = models.DateTimeField(default=datetime.now)
    # jobuploaddate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user


# Adding Startup
class Startuppost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)   #
    user = models.CharField(max_length=100)
    startupname = models.TextField()
    startupsector = models.TextField()
    startupbio = models.TextField()
    startuplocation = models.TextField()
    startupestablishment = models.TextField()
    startupcin = models.TextField()
    startupincorporation = models.TextField()
    startuppatents = models.TextField()
    startupwebsite = models.TextField()
    startuplinkedin = models.TextField()
    startupinstagram = models.TextField()
    startupyoutube = models.TextField()

    startupfoundername = models.TextField()
    startupfounderage = models.TextField()
    startupfoundereducation = models.TextField()
    startupfounderexperience = models.TextField()
    startupfounderequity = models.TextField()

    startupfocusarea = models.TextField()
    startupservices = models.TextField()

    # jobcompany = models.TextField(max_length=255, default='My Company')
    # jobcompany = models.TextField()
    # jobmodechoices = (
    #     ('office', 'Work From Office'),
    #     ('remote', 'Work From Home'),
    #     ('hybrid', 'Hybrid')
    # )
    # jobmode = models.CharField(max_length=20, default='Work From Office')
    # jobmode = models.TextField()
    # jobexperiencechoices = (
    #     ('belowtwo', '0 to 2 years'),
    #     ('twotofive', '2 to 5 years'),
    #     ('fivetoten', '5 to 10 years'),
    #     ('aboveten', 'Above 10 years')
    # )
    # jobexperience = models.CharField(max_length=20, choices=jobexperiencechoices, default='0 to 2 years')
    # jobexperience = models.TextField()
    # jobdepartment = models.TextField(max_length=240, default='Engineering')
    # jobuploaddate = models.DateTimeField(default=datetime.now)
    # jobuploaddate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user