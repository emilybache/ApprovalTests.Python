import unittest
import StringIO

from approvals.reporters import CommandlineReporter
from approvals.failures import ApprovalFailure

class CommandlineReporterTest(unittest.TestCase):
    def test_report(self):
        out = StringIO.StringIO()
        reporter = CommandlineReporter(out=out)
        failure = ApprovalFailure("received", "approved", False, "diff")
        reporter.report(failure)
        self.assertIn("mv received approved", out.getvalue())