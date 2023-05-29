from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost, FollowersCount, Jobpost, Startuppost
from itertools import chain
import random

# from datetime import datetime

# Create your views here.

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list =[]
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)
    
    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feef_list = list(chain(*feed))

    # User suggestions starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
        
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if x not in list(current_user)]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))
    
    return render(request, 'index.html', {'user_profile': user_profile, 'posts': feef_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:10]})

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='postnewjob')  
def postnewjob(request):
    return render(request, 'postnewjob.html')   

@login_required(login_url='postnewstartup')  
def postnewstartup(request):
    return render(request, 'postnewstartup.html')  

@login_required(login_url='signin')
def jobupload(request):

    if request.method == 'POST':
        user = request.user.username
        jobposition = request.POST['jobposition']
        joblocation = request.POST['joblocation']
        # jobtime = request.POST['jobtime']
        jobsalary = request.POST['jobsalary']
        jobabout = request.POST['jobabout']
        joblink = request.POST['joblink']

        jobcompany = request.POST['jobcompany']
        jobmode = request.POST['jobmode']
        jobexperience = request.POST['jobexperience']
        jobdepartment = request.POST['jobdepartment']

        # jobuploaddate = request.datetime.datetime

        new_jobpost = Jobpost.objects.create(user=user, jobposition=jobposition, joblocation=joblocation, 
                                             jobsalary=jobsalary, jobabout=jobabout, joblink=joblink, jobcompany=jobcompany, 
                                             jobmode=jobmode, jobexperience=jobexperience, jobdepartment=jobdepartment)
        new_jobpost.save()

        return redirect('/jobs')
    else:
        return redirect('/jobs')

@login_required(login_url='signin')
def startupupload(request):

    if request.method == 'POST':
        user = request.user.username
        startupname = request.POST['startupname']
        startupsector = request.POST['startupsector']
        startupbio = request.POST['startupbio']
        startuplocation = request.POST['startuplocation']
        startupestablishment = request.POST['startupestablishment']
        startupcin = request.POST['startupcin']
        startupincorporation = request.POST['startupincorporation']
        startuppatents = request.POST['startuppatents']
        startupwebsite = request.POST['startupwebsite']
        startuplinkedin = request.POST['startuplinkedin']
        startupinstagram = request.POST['startupinstagram']
        startupyoutube = request.POST['startupyoutube']
        startupfoundername = request.POST['startupfoundername']
        startupfounderage = request.POST['startupfounderage']
        startupfoundereducation = request.POST['startupfoundereducation']
        startupfounderexperience = request.POST['startupfounderexperience']
        startupfounderequity = request.POST['startupfounderequity']
        startupfocusarea = request.POST['startupfocusarea']
        startupservices = request.POST['startupservices']

        # jobuploaddate = request.datetime.datetime

        new_startuppost = Startuppost.objects.create(user=user, startupname=startupname, startupsector=startupsector, startupbio=startupbio, 
                                             startuplocation=startuplocation, startupestablishment=startupestablishment, startupcin=startupcin,
                                             startupincorporation=startupincorporation, startuppatents=startuppatents, startupwebsite=startupwebsite,
                                             startuplinkedin=startuplinkedin, startupinstagram=startupinstagram, startupyoutube=startupyoutube,
                                             startupfoundername=startupfoundername, startupfounderage=startupfounderage, startupfoundereducation=startupfoundereducation,
                                             startupfounderexperience=startupfounderexperience, startupfounderequity=startupfounderequity,
                                             startupfocusarea=startupfocusarea, startupservices=startupservices)
        new_startuppost.save()

        return redirect('/startups')
    else:
        return redirect('/startups')



@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_jobposts = Jobpost.objects.filter(user=pk)
    user_startupposts = Startuppost.objects.filter(user=pk)
    user_post_length = len(user_posts)
    user_jobpost_length = len(user_jobposts)
    user_startuppost_length = len(user_startupposts)

    

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_jobposts': user_jobposts,
        'user_startupposts': user_startupposts,
        'user_post_length': user_post_length,
        'user_jobpost_length': user_jobpost_length,
        'user_startuppost_length': user_startuppost_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following
    }
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user)

    else:
        return redirect('/')

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            establishment = request.POST['establishment']
            foundername = request.POST['foundername']
            founderage = request.POST['founderage']
            foundereducation = request.POST['foundereducation']
            website = request.POST['website']
            linkedin = request.POST['linkedin']
            experience = request.POST['experience']
            location = request.POST['location']
            equity = request.POST['equity']
            patents_published = request.POST['patents_published']
            cin_no = request.POST['cin_no']
            incorporation_type = request.POST['incorporation_type']
            # new added
            startupname = request.POST['startupname']
            instagramurl = request.POST['instagramurl']
            department = request.POST['department']
            youtubeurl = request.POST['youtubeurl']

            user_profile.profileimg = image
            user_profile.establishment = establishment
            user_profile.bio = bio
            user_profile.foundername = foundername
            user_profile.founderage = founderage
            user_profile.foundereducation = foundereducation
            user_profile.website = website
            user_profile.linkedin = linkedin
            user_profile.experience = experience
            user_profile.location = location
            user_profile.equity = equity
            user_profile.patents_published = patents_published
            user_profile.cin_no = cin_no
            user_profile.incorporation_type = incorporation_type
            # new added
            user_profile.startupname = startupname
            user_profile.instagramurl = instagramurl
            user_profile.department = department
            user_profile.youtubeurl = youtubeurl
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            establishment = request.POST['establishment']
            foundername = request.POST['foundername']
            founderage = request.POST['founderage']
            foundereducation = request.POST['foundereducation']
            website = request.POST['website']
            linkedin = request.POST['linkedin']
            experience = request.POST['experience']
            location = request.POST['location']
            equity = request.POST['equity']
            patents_published = patents_published.POST['patents_published']
            cin_no = cin_no.POST['cin_no']
            incorporation_type = incorporation_type.POST['incorporation_type']
            # new added
            startupname = startupname.POST['startupname']
            instagramurl = instagramurl.POST['instagramurl']
            department = department.POST['department']
            youtubeurl = youtubeurl.POST['youtubeurl']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.establishment = establishment
            user_profile.foundername = foundername
            user_profile.founderage = founderage
            user_profile.foundereducation = foundereducation
            user_profile.website = website
            user_profile.linkedin = linkedin
            user_profile.experience = experience
            user_profile.location = location
            user_profile.equity = equity
            user_profile.patents_published = patents_published
            user_profile.cin_no = cin_no
            user_profile.incorporation_type = incorporation_type
            # New added
            user_profile.startupname = startupname
            user_profile.instagramurl = instagramurl
            user_profile.department = department
            user_profile.youtubeurl = youtubeurl
            user_profile.save()

        return redirect('settings')
    return render(request, 'setting.html', {'user_profile': user_profile})

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # Create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')  
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')  
def about(request):
    return render(request, 'about.html')

 
def landing(request):
    return render(request, 'landing.html')

@login_required(login_url='signin')  
def insights(request):
    return render(request, 'insights.html')

@login_required(login_url='signin')  
def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacyPolicy.html')



@login_required(login_url='signin')  
def jobs(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    # user_following_list =[]
    jobfeed = []
    # user_following = FollowersCount.objects.filter(follower=request.user.username)

    #for users in user_following:
        #user_following_list.append(users.user)
    
    #for usernames in user_following_list:
    jobfeed_lists = Jobpost.objects.all()
    jobfeed.append(jobfeed_lists)

    jobfeef_list = list(chain(*jobfeed))

    # User suggestions starts
    # all_users = User.objects.all()
    # user_following_all = []

    # for user in user_following:
    #     user_list = User.objects.get(username=user.user)
    #     user_following_all.append(user_list)
        
    # new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    # current_user = User.objects.filter(username=request.user.username)
    # final_suggestions_list = [x for x in list(new_suggestions_list) if x not in list(current_user)]
    # random.shuffle(final_suggestions_list)

    # username_profile = []
    # username_profile_list = []

    # for users in final_suggestions_list:
    #     username_profile.append(users.id)

    # for ids in username_profile:
    #     profile_lists = Profile.objects.filter(id_user=ids)
    #     username_profile_list.append(profile_lists)

    # suggestions_username_profile_list = list(chain(*username_profile_list))
    
    return render(request, 'jobs.html', {'user_profile': user_profile, 'jobposts': jobfeef_list,})

    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)

    # jobfeed = []

    # jobposts = Jobpost.objects.all()
    # return render(request, 'jobs.html', {'user_profile': user_profile, 'jobposts': jobposts})


@login_required(login_url='signin')  
def startups(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    # user_following_list =[]
    startupfeed = []
    startupfeed_lists = Startuppost.objects.all()
    startupfeed.append(startupfeed_lists)

    startupfeef_list = list(chain(*startupfeed))
    
    return render(request, 'startups.html', {'user_profile': user_profile, 'startupposts': startupfeef_list,})






    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)

    # jobfeed = []

    # jobposts = Jobpost.objects.all()
    # return render(request, 'jobs.html', {'user_profile': user_profile, 'jobposts': jobposts})


# @login_required(login_url='signin')  
# def startups(request):
#     return render(request, 'startups.html')

@login_required(login_url='signin')  
def home(request):
    return render(request, 'home.html')

@login_required(login_url='signin')  
def profilestartup(request):
    return render(request, 'profilestartup.html')

def terms(request):
    return render(request, 'terms.html')




