from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy, reverse

# Create your tests here.
# class MeetingTest(TestCase):
#     def setUp(self):
#         self.type=Meeting(meetingtitle='meeting 1')

#     def test_meetingstring(self):
#         self.assertEqual(str(self.type), 'meeting 1')

#     def test_tablename(self):
#         self.assertEqual(str(Meeting._meta.db_table), 'meeting')

# class MeetingMinutesTest(TestCase):
#     def setUp(self):
#         self.type=MeetingMinutes(minutes='1')

#     def test_meetingminutesstring(self):
#         self.assertEqual(str(self.type), '1')

#     def test_tablename(self):
#         self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

# class ResourceTest(TestCase):
#     def setUp(self):
#         self.type=Resource(resourcename='resource 1')

#     def test_resourcestring(self):
#         self.assertEqual(str(self.type), 'resource 1')
    
#     def test_tablename(self):
#         self.assertEqual(str(Resource._meta.db_table), 'resource')

# class EventTest(TestCase):
#     def setUp(self):
#         self.type=Event(eventtitle='event 1')
        
#     def test_eventstring(self):
#         self.assertEqual(str(self.type), 'event 1')
    
#     def test_tablename(self):
#         self.assertEqual(str(Event._meta.db_table), 'event')

class New_Resource_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource=Resource.objects.create(resourcename='resource 1')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newresource/')