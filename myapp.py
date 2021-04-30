import json
import requests

URL_podcast="http://127.0.0.1:8000/podcast/"
URL_song = "http://127.0.0.1:8000/song/"
URL_story = "http://127.0.0.1:8000/story/"
URL_get = "http://127.0.0.1:8000/get_audio/podcast/"
URL_post = "http://127.0.0.1:8000/post_audio/story/"
URL_put = "http://127.0.0.1:8000/update_audio/song/2/"
URL_delete = "http://127.0.0.1:8000/delete_audio/story/2/"
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    #changing python data into json data
    json_data = json.dumps(data)
    #change URL accordingly if you're using podcast, song or story
    r=requests.get(url = URL_get, data = json_data)
    #extracting this data
    data = r.json()
    print(data)

# get_data()

def post_data():
    data = {
        # 'podcast_name': 'Russian Roulette',
        # 'podcast_narrator': 'Tim Matthew'
        # 'song_name': 'Bad liar',
        # 'song_artist': 'Billie Eilish'
        'story_name': 'The Animal Farm',
        'story_author':'George Orwell',
        'story_narrator':'Tim',
    }
    json_data = json.dumps(data)
    r=requests.post(url = URL_post, data = json_data)
    #extracting this data
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        # 'id': 4,
        'song_artist': 'Hailey Kyuoko'
    }
    json_data = json.dumps(data)
    r=requests.put(url = URL_put, data = json_data)
    #extracting this data
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id': 1
    }
    json_data = json.dumps(data)
    r=requests.delete(url = URL_delete, data = json_data)
    #extracting this data
    data = r.json()
    print(data)

# delete_data()