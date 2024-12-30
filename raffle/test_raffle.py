import unittest


class TestRaffle(unittest.TestCase):

    def test_when_kids_have_no_preference_instruments_are_assigned_randomly(self):
        repository = KidsRepository()

        kids = repository.get_kids_information()

        self.assertEqual(13, len(kids), "Should have 13 kids")
