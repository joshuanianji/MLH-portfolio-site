import unittest
from peewee import *
from app import TimelinePost

test_db = SqliteDatabase(':memory:')

MODELS = [TimelinePost]

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name="John Doe",
                                         email="john@example.com",
                                         content="Hello World, I'm John")
        assert first_post.id == 1
        second_post = TimelinePost.create(name="Jame Dane",
                                          email="jame@example.com",
                                          content="Hello World, I'm Jame")
        assert second_post.id == 2

        assert TimelinePost.get_by_id(1) == first_post
        assert TimelinePost.get_by_id(2) == second_post
