from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='meeting 1')

    def test_meetingstring(self):
        self.assertEqual(str(self.type), 'meeting 1')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=MeetingMinutes(minutes='1')

    def test_meetingminutesstring(self):
        self.assertEqual(str(self.type), '1')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='resource 1')

    def test_resourcestring(self):
        self.assertEqual(str(self.type), 'resource 1')
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='event 1')
        
    def test_eventstring(self):
        self.assertEqual(str(self.type), 'event 1')
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')