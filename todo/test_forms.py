from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({"name": ""})
        # form is not valid with empty name
        self.assertFalse(form.is_valid())
        # make sure there is an error for the missing name
        self.assertIn("name", form.errors.keys())
        # make sure the error message is correct
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_is_not_required(self):
        form = ItemForm({"name": "Test item"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        # make sure the form fields where not changed
        self.assertEqual(form.Meta.fields, ["name", "done"])
