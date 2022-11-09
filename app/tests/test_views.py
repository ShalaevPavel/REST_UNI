from django.test import TestCase, Client
from django.urls import reverse
from app.models import String_Concatenation
import json


class TestViews(TestCase):

    def test_POST_adds_new_ToDo_object_is_null(self):
        self.assertEquals(String_Concatenation.objects.all().count(), 0)
