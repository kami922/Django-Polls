from django.shortcuts import render,redirect
from .forms import CreatePollForm
from .models import Polls
from django.shortcuts import HttpResponse



# Create your views here.
def home(request):
    polls = Polls.objects.all()
    params = {
        "polls":polls
    }
    return render(request,"polls/home.html",params)


def create(request):
    if request.method == "POST":
        form= CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreatePollForm()
    params = {"form":form}
    return render(request,"polls/create.html",params)


def vote(request,poll_id):
    poll = Polls.objects.get(pk=poll_id)
    if request.method == "POST":
        selected_option = request.POST["poll"]
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == "option3":
            poll.option_three_count += 1
        else:
            HttpResponse(400,"invalid Form")

        poll.save()
        return redirect("result",poll.id)
    params = {
        "poll":poll
        }
    return render(request,"polls/vote.html",params)


def result(request,poll_id):
    poll = Polls.objects.get(pk = poll_id)
    params = {
        'poll':poll
              }
    return render(request,"polls/results.html",params)