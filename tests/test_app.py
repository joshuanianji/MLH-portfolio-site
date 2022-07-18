import unittest
import os
from peewee import OperationalError
from app import mydb as db, app, TimelinePost

os.environ['TESTING'] = 'true'

timeline_endpoint = "/api/timeline_post"


class AppTestCase(unittest.TestCase):

    def setUp(self):
        try:
            self.client = app.test_client()
            db.connect()
            db.create_tables([TimelinePost])
        except OperationalError as e:
            print('Test app operational error!', e)
            self.client = app.test_client()

    def tearDown(self):
        db.drop_tables([TimelinePost])
        db.close()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Home - Portfolio</title>" in html
        assert "Joshua Ji" in html

    def test_timeline(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Timeline - Portfolio" in html

        response = self.client.get(timeline_endpoint)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 0

        post_data = {
            'name': 'Jie Chen',
            'email': 'jie@fellowship.com',
            'content': 'Hi from Jie!'
        }

        response_post = self.client.post(timeline_endpoint, data=post_data)
        assert response_post.status_code == 200
        assert response_post.is_json
        json = response_post.get_json()

        for k in post_data:
            assert post_data[k] == json[k]

    def test_malformed_timeline_post(self):
        # Missing name
        response = self.client.post(timeline_endpoint,
                                    data={
                                        "email": "john@example.com",
                                        "content": "Hello World, I'm John"
                                    })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Missing name" in html

        # Missing/invalid email
        response = self.client.post(timeline_endpoint,
                                    data={
                                        "name": "John Doe",
                                        "content": "Hello World, I'm John"
                                    })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Missing email or invalid email" in html

        # Missing content
        response = self.client.post(timeline_endpoint,
                                    data={
                                        "name": "John Doe",
                                        "email": "john@hi.com",
                                    })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Missing content" in html