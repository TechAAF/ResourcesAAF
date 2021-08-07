from contests.views import contests
from django.shortcuts import render, HttpResponse
from research_centers import models

# Fetch all the research centers
def index(request):

    research_centers = models.Research_Center.objects.all()
    

    context = {
        'research_centers': research_centers
    }

    return render(request, 'research_centers/research_centers.html', context)

# to fetch a particular research center
def get_research_center(request, center_id):

    center = models.Research_Center.objects.get(pk=center_id)

    # that centre's activities
    activities = models.Activity.objects.filter(research_center = center_id)

    print(activities)

    print(center)

    context = {
        'center': center,
        'activities': activities[:3],
    }

    return render(request, 'research_centers/individual_center.html', context)

# Research center activities

def get_research_center_activities(request, center_id):
    center = models.Research_Center.objects.get(pk=center_id)
    activities = models.Activity.objects.filter(research_center = center_id)

    context = {
        'center': center,
        'activities': activities
    }

    return render(request, 'research_centers/center_activities.html', context)


# Show all the activities of the research center
def show_activity(request, center_id,activity_id):
    
    center = models.Research_Center.objects.get(pk=center_id)
    activity = models.Activity.objects.get(pk=activity_id)



    
    print(activity)

    context = {
        'center': center,
        'activity': activity
    }

    return render(request, 'research_centers/individual_activity.html', context)

