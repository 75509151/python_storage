# coding: utf-8

from mock import Mock, MagicMock, patch
import unittest
from client import visit_ustack
from contextlib import nested
from class_rm import RemovalService


class RemovalServiceTestCase(unittest.TestCase):

    @patch('class_rm.os.path')
    @patch('class_rm.os')
    def test_rm_class(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("any path")

        mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
