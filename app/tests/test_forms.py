from django.test import SimpleTestCase
from app.forms import String_ConcatenationForm, String_MultiplicationForm


class TestForms(SimpleTestCase):
    def test_todo_form_valid_data_mult(self):
        form = String_MultiplicationForm(data={
            "string_for_multiplication": "run",
            "n": 5
        })
        self.assertTrue(form.is_valid())

    def test_no_data_in_form_mult(self):
        form = String_MultiplicationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)



    def test_todo_form_valid_data_conc(self):
        form = String_ConcatenationForm(data={
            "string1": "a",
            "string2": "b"
        })
        self.assertTrue(form.is_valid())

    def test_no_data_in_form_conc_for_blank_equals_true(self):
        form = String_ConcatenationForm(data={})

        self.assertTrue(form.is_valid())
