from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.shortcuts import reverse, redirect, render
from django.http.response import JsonResponse
from django.shortcuts import redirect

from courses import models

import requests, json

def index(request):
    return redirect('/courses')

def courses(request):
    Courses= models.Course.objects.all()
    Categories = models.Category.objects.all()

    requested_filters = request.GET.getlist('filter_list')

    print(requested_filters)
    filtered_courses = []
    
    if(len(requested_filters) > 0):
        for course in Courses:
            curr_categories = course.category.all()

            for category in curr_categories:
                if category.name in requested_filters:
                    filtered_courses.append(course)
                    break          
        print("Hello from filter if")  
        Courses = filtered_courses

    context = {
        "courses": Courses,
        'filters': Categories,
        'active_filters': requested_filters
    }
    return render(request, 'courses/courses.html', context)




# Helper method
# Method to get Playlist ID from URL
# TODO: Add more checks on URL
def get_playlist_id(URL):
    INITIAL = 'https://www.youtube.com/playlist?list='
    if INITIAL in URL:
        index = URL.find(INITIAL)+len(INITIAL)
        ID = URL[index:]

        return True, ID
    return False, None

# Function to fetch the videos of a particular playlist

def get_videos(url):
    playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    List_ID = get_playlist_id(url)
    params = {
        'part': 'snippet',
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'playlistId': List_ID,
        'maxResults':50,
    }
    videos = []
    results = requests.get(playlist_url,params).json()
    next_page_data = results
    while('nextPageToken' in next_page_data):
        # Get all videos from multiple pages.
        params['pageToken'] = next_page_data['nextPageToken']
        next_page_data = requests.get(playlist_url, params=params).json()
        results['items'] += (next_page_data['items'])

    return results

def course_playlist(request, course_id):    
    course = models.Course.objects.get(pk=course_id)

    playlist = get_videos(course.playlist_id)['items']

    print(playlist[0]['snippet'])


    current_video = {}

    current_video['description'] = playlist[0]['snippet']['description']

    current_video['video_id'] = request.GET.get('video-id')

    if current_video['video_id'] is None:
        current_video['video_id'] = playlist[0]['snippet']['resourceId']['videoId']
        


    context = {
        'course': course,
        'playlist': playlist,
        'current_video': current_video,
    }

    return render(request, 'courses/course_playlist.html', context)

# def details(request, course_id):
#     course=models.Course.objects.get(pk=course_id)
#     return render(request,"courses/course_playlist.html",{"course":course})

