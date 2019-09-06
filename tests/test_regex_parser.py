import unittest
from tigr.lib.parser.regex_parser import RegexParser
from tigr.lib.parser.regex_parser import ParseException
from tigr.lib.drawer.turtle_drawer import TurtleDrawer


class TestCaseRegexParser(unittest.TestCase):

    def setUp(self):
        self.instance = RegexParser(TurtleDrawer)
    
    def test_parse(self):
        try:
            self.instance.parse(['cs okoks'])
        except Exception as e:
            self.fail('"parse()" should not raise any exceptions')
        
        try:
            self.instance.parse(['#', '\n\n\n'])
        except Exception as e:
            self.fail('"parse()" should not raise any exceptions')

if __name__ == '__main__':
    unittest.main()
