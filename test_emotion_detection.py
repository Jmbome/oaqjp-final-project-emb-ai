import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion_detector function.
    """

    def test_joy_detection(self):
        """Test for the sentence 'I am glad this happened' should return 'joy'."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_detection(self):
        """Test for the sentence 'I am really mad about this' should return 'anger'."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_detection(self):
        """Test for the sentence 'I feel disgusted just hearing about this' should return 'disgust'."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_detection(self):
        """Test for the sentence 'I am so sad about this' should return 'sadness'."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_detection(self):
        """Test for the sentence 'I am really afraid that this will happen' should return 'fear'."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

