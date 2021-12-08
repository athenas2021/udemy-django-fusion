import uuid
from django.test import TestCase
from model_mommy import mommy


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEquals(str(self.service), self.service.service)


class PositionTestCase(TestCase):

    def setUp(self):
        self.position = mommy.make("Position")

    def test_str(self):
        self.assertEquals(str(self.position), self.position.position)

class TeamTestCase(TestCase):

    def setUp(self):
        self.team = mommy.make("Team")

    def test_str(self):
        self.assertEquals(str(self.name), self.team.name)