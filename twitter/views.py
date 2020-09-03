from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView,View

from .forms import *

class ThoughtSharing(View):
    def get(self, *args, **kwargs):
        thoughts = ThoughtTweet.objects.order_by('-id')
        if self.request.user.is_authenticated :
            form = TweetForm()
            profile = Profile.objects.get(user=self.request.user)
        else:
            form = ''
            profile = ''

        users = Profile.objects.all()

        context = {
            'thoughts':thoughts,
            'form':form,
            'profile':profile,
            'users':users,
        }

        return render(self.request, "twitter/tweet.html", context)

    def post(self, *args, **kwargs):
        form = TweetForm(self.request.POST)
        user = Profile.objects.get(user=self.request.user)
        if form.is_valid():
            thought = form.cleaned_data.get('tweet')

            tweeting = ThoughtTweet(
                user = user,
                tweet = thought
            )
            tweeting.save()

        return redirect('/')

@login_required
def likeTweet(request, pk):
    tweet = get_object_or_404(ThoughtTweet, id=pk)
    
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)

    return redirect('/')




class RegisterView(FormView):
    template_name = 'twitter/signup.html'
    form_class = SignUpForm

    def get(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        User_form = self.get_form(form_class)
        profile_form = ProfileForm()
        context = {
        'form1':User_form,
        'form2':profile_form
        }
        return render(self.request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        User_form = self.get_form(form_class)
        profile_form = ProfileForm(self.request.POST, self.request.FILES)
        if (User_form.is_valid() and profile_form.is_valid()):
            return self.form_valid(User_form,profile_form)
        else:
            return redirect("/signup/")


    def get_success_url(self,**kwargs):
        return ('success')


    def form_valid(self,User_form,profile_form):
        self.object=User_form.save()
        self.object.save()
        profile_obj= profile_form.save(commit=False)
        profile_obj.user = self.object
        profile_obj.save()
        return redirect('/login/')

    def form_invalid(self,User_form,profile_form):
        context = {
        'form1':User_form,
        'form2':profile_form
        }
        return render(self.request,self.template_name,context)