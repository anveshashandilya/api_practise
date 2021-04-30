from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from .models import Podcast, Song, Story
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

@method_decorator(csrf_exempt, name = 'dispatch')
class SongAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #get the id if id is present in request else return none in id
        id = pythondata.get('id', None)
        if id is not None:
            song = Song.objects.get(id = id)
            serializer = SongSerializer(song)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        song = Song.objects.all()
        serializer = SongSerializer(song, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = SongSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe = False)
        #When data is not valid then return error message
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        song = Song.objects.get(id = id)
        #For partial update
        serializer = SongSerializer(song, data = pythondata, partial = True)
        #For full update, required all data from client side
        # serializer = PodcastSerializer(pod, data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated!'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe = False)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        song = Song.objects.get(id = id)
        song.delete()

        res = {'msg': 'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(res, safe = False)


@method_decorator(csrf_exempt, name = 'dispatch')
class StoryAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #get the id if id is present in request else return none in id
        id = pythondata.get('id', None)
        if id is not None:
            story = Story.objects.get(id = id)
            serializer = StorySerializer(story)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        story = Story.objects.all()
        serializer = StorySerializer(story, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StorySerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe = False)
        #When data is not valid then return error message
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        story = Story.objects.get(id = id)
        #For partial update
        serializer = StorySerializer(story, data = pythondata, partial = True)
        #For full update, required all data from client side
        # serializer = PodcastSerializer(pod, data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated!'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe = False)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        story = Story.objects.get(id = id)
        story.delete()

        res = {'msg': 'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(res, safe = False)






@csrf_exempt
def podcast_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #get the id if id is present in request else return none in id
        id = pythondata.get('id', None)
        if id is not None:
            pod = Podcast.objects.get(id = id)
            serializer = PodcastSerializer(pod)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        pod = Podcast.objects.all()
        serializer = PodcastSerializer(pod, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = PodcastSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe = False)
        #When data is not valid then return error message
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        pod = Podcast.objects.get(id = id)
        #For partial update
        serializer = PodcastSerializer(pod, data = pythondata, partial = True)
        #For full update, required all data from client side
        # serializer = PodcastSerializer(pod, data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated!'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe = False)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        pod = Podcast.objects.get(id = id)
        pod.delete()

        res = {'msg': 'Data Deleted'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(res, safe = False)


# class CreateView(generics.ListCreateAPIView):
#     '''
#     -Defines the create behaviour (POST) of API
#     -Handles reverse(create)
#     -The 'ListCreateAPIView' is a generic view which provides GET(list all) and create
#     '''
#     # audio_type = audio_type
#     if self.kwargs['audio_type'] == 'podcast':
#         queryset = Podcast.objects.all()
#         serializer_class = PodcastSerializer
#     # elif self.kwargs['audio_type'] == 'song':


#     def perform_create(self, serializer):
#         """Save post data when creating a new bucketlist."""
#         serializer.save()
class GetAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #get the id if id is present in request else return none in id
        id = pythondata.get('id', None)
        if id is not None:
            song = Song.objects.get(id = id)
            serializer = SongSerializer(song)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        song = Song.objects.all()
        serializer = SongSerializer(song, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')



@csrf_exempt
def final_api(request, audio_type, audio_id = None):
    if request.method == 'GET':
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        #get the id if id is present in request else return none in id
        if audio_id is not None:
            if audio_type == 'podcast':
                pod = Podcast.objects.get(id = audio_id)
                serializer = PodcastSerializer(pod)
            elif audio_type == 'song':
                song = Song.objects.get(id = audio_id)
                serializer = SongSerializer(song)
            elif audio_type == 'story':
                story = Story.objects.get(id = audio_id)
                serializer = StorySerializer(story)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json', status = 200)


        if audio_type == 'podcast':
            pod = Podcast.objects.all()
            serializer = PodcastSerializer(pod, many = True)
        elif audio_type == 'song':
            song = Song.objects.all()
            serializer = SongSerializer(song, many=True)
        elif audio_type == 'story':
            story = Story.objects.all()
            serializer = StorySerializer(story, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        if audio_type == 'podcast':
            serializer = PodcastSerializer(data = pythondata)

        elif audio_type == 'song':
            serializer = SongSerializer(data = pythondata)

        elif audio_type == 'story':
            serializer = StorySerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json', status=201)
            # return JsonResponse(res, safe = False)
        #When data is not valid then return error message
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json', status=201)

    if request.method == 'PUT':

            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            # id = pythondata.get('id')
            if audio_type == 'podcast':
                pod = Podcast.objects.get(id = audio_id)
                serializer = PodcastSerializer(pod, data = pythondata, partial = True)
            elif audio_type == 'song':
                song = Song.objects.get(id = audio_id)
                serializer = SongSerializer(song, data = pythondata, partial = True)
            if audio_type == 'story':
                story = Story.objects.get(id = audio_id)
                serializer = StorySerializer(story, data = pythondata, partial = True)



            #For partial update
            # serializer = PodcastSerializer(pod, data = pythondata, partial = True)
            #For full update, required all data from client side
            # serializer = PodcastSerializer(pod, data = pythondata)
            if serializer.is_valid():
                serializer.save()
                res = {'msg' : 'Data Updated!'}
                # json_data = JSONRenderer().render(res)
                # return HttpResponse(json_data, content_type = 'application/json')
                return JsonResponse(res, safe = False)
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type = 'application/json', status=200)

    if request.method == 'DELETE':
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        # id = pythondata.get('id')
        if audio_type == 'podcast':
            pod = Podcast.objects.get(id = audio_id)
            pod.delete()
        if audio_type == 'song':
            song = Song.objects.get(id = audio_id)
            song.delete()
        if audio_type == 'story':
            story = Story.objects.get(id = audio_id)
            story.delete()

        res = {'msg': 'Data Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json', status = 204)
        # return JsonResponse(res, safe = False)