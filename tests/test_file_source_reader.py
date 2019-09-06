import io
import unittest
from collections.abc import Iterable
from tigr.lib.source_reader.file_source_reader import FileSourceReader
from tigr.lib.parser.regex_parser import RegexParser
from tigr.lib.drawer.turtle_drawer import TurtleDrawer


class TestCaseFileSourceReader(unittest.TestCase):

    def setUp(self):
        pseudo_file = io.StringIO('E 100\nS 100')
        parser = RegexParser
        drawer = TurtleDrawer
        self.instance = FileSourceReader(
            parser(drawer()), optional_file_name=pseudo_file)
    
    def test_go(self):
        try:
            self.instance.go()
        except Exception:
            self.fail('go() should not raise any exceptions')
        else:
            self.assertTrue(isinstance(self.instance.source, Iterable))