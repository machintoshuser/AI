# Example 4: mocking

"""
Using an example where we can do some mocking. Here we're reading in a file and applying an operation (getting unique chars).
"""

def unique_chars_from_file(filepath):
    """
    Assume this function takes in some file that I read in and does something as an output. For testing purposes, we don't want to keep the reference to that file, so we'll mock it.
    :return:
    """
    with open(filepath) as f:
        contents = f.read()
    print(
        contents
    )  # set a break point here to see what "f" is - once in the test, once in the assert statement
    return len(set(contents))


from unittest import TestCase
from unittest.mock import patch, mock_open


assert unique_chars_from_file("temp.txt") == 13


class TestContextManager(TestCase):
    def test_context_manager(self):
        with patch("builtins.open", mock_open(read_data="myfakedatax")) as mock_file:
            self.assertEqual(unique_chars_from_file("fake_path"), 8)

    @patch(
        "builtins.open", new_callable=mock_open, read_data="myfakedatax"
    )  # exact same code as before, but we're using the decorator syntax!
    def test_context_manager_v2(self, mock_file):
        self.assertEqual(unique_chars_from_file("fake_path"), 8)
