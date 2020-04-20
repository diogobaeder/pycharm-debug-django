from django.test import TestCase


class TestFoo(TestCase):
    def test_something(self):
        foo = 1
        bar = 2

        self.assertEqual(bar, foo * 2)
