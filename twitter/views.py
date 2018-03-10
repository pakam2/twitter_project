from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Tweet
from .forms import TweetForm, LoginForm

# Create your views here.


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Nie ma takiego użytkownika")



class MainView(View):

    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'main.html', {'tweets': tweets})


class AddTweetView(LoginRequiredMixin, View):

    def get(self, request):
        form = TweetForm()
        return render(request, 'add_new_tweet.html', {'form': form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('/')



class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
