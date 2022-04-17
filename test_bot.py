from unittest import TestCase
from image_manager import *

class TestBot(TestCase):
    
    def setUp(self):
        pass

    def test_folder_search_should_return_a_valid_response_when_an_existing_folder_name_is_passed(self):
        response = folder_search(folder_name="miku")
        self.assertNotEqual(response, "Error, no such directory!")
    def test_folder_search_should_return_an_invalid_response_when_an_non_existing_folder_name_is_passed(self):
        response = folder_search(folder_name="2333282920202902")
        self.assertEqual(response, "Error, no such directory!")

    def test_integration_folder_search_get_image_should_work_together(self):
        path = folder_search(folder_name="miku")
        response = get_image(path)

        self.assertIsNotNone(response)

    def test_get_image_should_return_default_archive_if_invalid_path_is_passed(self):
        path = folder_search(folder_name="12121221")
        response = get_image(path)
        
        self.assertEqual(response, "images/default.png")
