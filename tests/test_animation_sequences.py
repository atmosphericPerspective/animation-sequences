import pathlib
import unittest
from unittest.mock import patch, call
from animation_sequences import find_animation_sequences


@patch('builtins.print')
class TestFindAnimationSequences(unittest.TestCase):
    path = pathlib.Path(__file__).resolve().parent

    def test_dir_no_exists(self, _mock_print):
        self.assertRaises(NotADirectoryError,
                          find_animation_sequences,
                          str(self.path / 'files/abcdefghj'))

    def test_empty_directory(self, mock_print):
        find_animation_sequences(str(self.path / 'files/empty_directory'))
        self.assertEqual(mock_print.mock_calls, [])

    def test_single_file(self, mock_print):
        find_animation_sequences(str(self.path / 'files/single_file'))
        self.assertEqual(mock_print.mock_calls, [call("renderer001: 0")])

    def test_single_range(self, mock_print):
        find_animation_sequences(str(self.path / 'files/single_range'))
        self.assertEqual(mock_print.mock_calls, [call("renderer001: 2000-2003")])

    def test_single_gap(self, mock_print):
        find_animation_sequences(str(self.path / 'files/single_gap'))
        self.assertEqual(mock_print.mock_calls, [call("renderer001: 3, 10-11")])

    def test_many_gap(self, mock_print):
        find_animation_sequences(str(self.path / 'files/many_gap'))
        self.assertEqual(mock_print.mock_calls, [call("renderer001: 3-4, 1004, 2004-2006, 9999")])

    def test_many_names(self, mock_print):
        find_animation_sequences(str(self.path / 'files/many_names'))
        self.assertEqual(mock_print.mock_calls, [call("renderer001: 3-4, 1004, 2004-2006, 9999"),
                                                 call("renderer002: 3, 10-11")])

    def test_unknown_files(self, mock_print):
        find_animation_sequences(str(self.path / 'files/unknown_files'))
        self.assertEqual(mock_print.mock_calls, [call("renderer001: 3, 10-11")])

    def test_special_names(self, mock_print):
        find_animation_sequences(str(self.path / 'files/special_names'))
        self.assertEqual(mock_print.mock_calls, [call("a b: 1"),
                                                 call("a-b: 1"),
                                                 call("a_b: 1")])


if __name__ == '__main__':
    unittest.main()
