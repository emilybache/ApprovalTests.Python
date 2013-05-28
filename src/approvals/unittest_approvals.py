import unittest
import inspect
import os

import approval_tests
from namers import SimpleNamer


class ApprovalsTestCase(unittest.TestCase):
    def setUp(self):
        test_case_name = unittest.TestCase.id(self)
        test_case_name = test_case_name.replace(".", "_")
        namer = SimpleNamer(test_case_name, os.path.dirname(inspect.getfile(self.__class__)))
        self.Approvals = approval_tests.Approvals(namer)