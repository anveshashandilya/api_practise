from django.test import TestCase, Client
from .models import Podcast
from django.http import HttpRequest

# View test
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from rest_framework import status

# Create your tests here.

# class PodcastTestCase(TestCase):

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.podcast_name = "podcast name given by user/test"
#         print(self.podcast_name)
#         self.podcast = Podcast(podcast_name=self.podcast_name) # Creates a podcast model with the given NAME


#     def test_model_can_create_a_podcast(self):
#         """Test if the podcast model can create a podcast with the given podcast_name."""
#         print('--------------->>>>>>>>>>>>')
#         old_count = Podcast.objects.count()#Count how many data objs in the beginning
#         print(old_count)
#         self.podcast.save()#save the new data obj
#         new_count = Podcast.objects.count()#Count how many data objs after saving
#         print(new_count)
#         self.assertNotEqual(old_count, new_count) # see if old_count and new_count NOT EQUAL. if so, test is passed.


class ViewTestCase(TestCase):
    '''
    Test Program for API app views
    '''
    def setUp(self, audio_type='podcast'):
        '''
        Define the test client and other test variables
        '''
        self.client = APIClient()
        # self.audio_type = 'podcast'
        self.podcast_data = {'podcast_name' : 'Go to Italy',
        'podcast_narrator':'Neville'}
        self.response = self.client.post(
                            reverse('create', kwargs={'audio_type':'podcast'}),
                            self.podcast_data,
                            format="json")

    def test_api_can_create_a_podcast(self):
        """
            Test if api has podcast creation ability.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        #  See if response status code is EQUAL to 201. if so, Test is passed.



    def test_api_can_get_a_bucketlist(self):
        """
            Test if the api can get/fetch a chosen podcast
        """
        pod = Podcast.objects.get()
        response = self.client.get(
                    reverse('get_id', kwargs={
                        'audio_type':'podcast',
                        'audio_id': pod.id, 
                        }),
                    format="json")
                        # pk : unique ID key in database
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response, bucketlist)


    def test_api_can_update_bucketlist(self):
        """
            Test if api can update a chosen bucketlist by user
        """
        change_bucketlist = {'podcast_name': 'Hill Side Stories'}
        pod = Podcast.objects.get()
        res = self.client.put(
                reverse('update', kwargs={'audio_type': 'podcast',
                'audio_id': pod.id }),
                change_bucketlist,
                format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

# URL_post = "http://127.0.0.1:8000/post_audio/podcast/"
# class StudentTests(APITestCase):
#     def setUp(self):
#         self.data = {

#             "podcast_name": "Internet says so",
#             "podcast_narrator": "Neville"}
#         self.response = self.client.post(
#                     reverse('create'),
#                     url = URL_post,
#                     self.data,
#                     format="json")


#     def test_api_create_student(self):
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#         # self.assertEqual(Student.objects.count(), 1)
#         # self.assertEqual(Student.objects.get().name, 'Neville')

    def test_api_can_delete_bucketlist(self):
        """
            Test if api can delete a chosen bucketlist
        """
        pod = Podcast.objects.get()
        res = self.client.delete(
                reverse('delete', kwargs={'audio_type':'podcast', 'audio_id': pod.id}),
                format="json",
                follow=True
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

