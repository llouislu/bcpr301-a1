import unittest
from collections.abc import Iterable
from tigr.lib.source_reader.prompt_source_reader import PromptSourceReader
from tigr.lib.parser.regex_parser import RegexParser
from tigr.lib.drawer.turtle_drawer import TurtleDrawer


class TestCasePromptSourceReader(unittest.TestCase):

    def setUp(self):
        parser = RegexParser
        drawer = TurtleDrawer
        self.instance = PromptSourceReader(
            parser(drawer()), optional_file_name=None)

    def test_go(self):
        self.assertFalse(self.instance.onecmd('E 100.1'))
        self.assertTrue(self.instance.onecmd('quit'))