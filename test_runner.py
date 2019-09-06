import unittest
from tests.test_turtle_drawer import TestCasetTurtleDrawer
from tests.test_tkinter_drawer import TestCasetTkinterDrawer
from tests.test_regex_parser import TestCaseRegexParser
from tests.test_peg_parser import TestCasePegParser
from tests.test_file_source_reader import TestCaseFileSourceReader
from tests.test_prompt_source_reader import TestCasePromptSourceReader

the_suite = unittest.TestSuite()

the_suite.addTest(unittest.makeSuite(TestCasetTurtleDrawer))
the_suite.addTest(unittest.makeSuite(TestCasetTkinterDrawer))
the_suite.addTest(unittest.makeSuite(TestCaseRegexParser))
the_suite.addTest(unittest.makeSuite(TestCasePegParser))
the_suite.addTest(unittest.makeSuite(TestCaseFileSourceReader))
the_suite.addTest(unittest.makeSuite(TestCasePromptSourceReader))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(the_suite)
