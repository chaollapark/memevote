from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Meme

class MemeModelTests(TestCase):

    def test_create_meme(self):
        """Test creating a new Meme instance with an image."""
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        meme = Meme.objects.create(image=image)

        # Check that the meme object was created successfully
        self.assertIsNotNone(meme)
        # Check that the image was saved and the path is as expected
        self.assertTrue(meme.image.name.startswith('memes/'))  