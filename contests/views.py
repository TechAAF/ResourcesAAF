from django.shortcuts import redirect, render
from contests import models

# Create your views here.

def contests(request):

    Contests = models.Contest.objects.all()
    Categories = models.Category.objects.all()

    requested_filters = request.GET.getlist('filter_list')

    print(requested_filters)
    filtered_contests = []
    
    if(len(requested_filters) > 0):
        for contest in Contests:
            curr_categories = contest.category.all()

            for category in curr_categories:
                if category.name in requested_filters:
                    filtered_contests.append(contest)
                    break          
        print("Hello from filter if")  
        Contests = filtered_contests

    context = {
        'contests': Contests,
        'filters': Categories,
        'active_filters': requested_filters
    }

    return render(request, 'contests/contests.html', context)

def contests_individual(request, contest_id):

    contest = models.Contest.objects.get(pk=contest_id)
    #add filter for status
    submissions=models.Submission.objects.all().filter(contest=contest_id)

    print(contest)

    context = {
        'contest': contest,
        'submissions': submissions
    }

    return render(request, 'contests/individual_contest.html', context)

def ContestSubmit(request, contest_id):
    models.Submission.objects.create(user_id=request.user, caption=request.POST['caption'], image_url=request.POST['image_url'], video_url=request.POST['video_url'], contest=models.Contest.objects.get(pk=contest_id))
    return redirect("/contests/"+str(contest_id))

def SubmissionLike(request, submission_id):
    submission= models.Submission.objects.get(pk=submission_id)
    if request.user in submission.likes.all():
        print("removed")
        submission.likes.remove(request.user)
    else:
        submission.likes.add(request.user)
        print("added")
    submission.save()
    return redirect("/contests/"+str(submission.contest.id))