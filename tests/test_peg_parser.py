import unittest
from tigr.lib.parser.peg_parser import PegParser
from tigr.lib.drawer.turtle_drawer import TurtleDrawer


class TestCasePegParser(unittest.TestCase):

    def setUp(self):
        self.instance = PegParser(TurtleDrawer)
    
    def test_parse(self):
        raw_sources = [
            ['cs okoks'],
            ['#', '\n\n\n'],
            ['', '']
        ]
        for test_statement in raw_sources:
            try:
                self.instance.parse(test_statement)
            except Exception:
                self.fail('"parse()" should not raise any exceptions')

        self.instance.parse(['E 100.111'])
        self.assertEqual(self.instance.command, 'E')
        self.assertEqual(self.instance.data, 100.111)

if __name__ == '__main__':
    unittest.main()
