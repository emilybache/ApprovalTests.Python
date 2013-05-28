import unittest
import os

from approvals.unittest_approvals import ApprovalsTestCase
from approvals.failures import ApprovalError


class ApprovalsTest(ApprovalsTestCase):

    def setUp(self):
        ApprovalsTestCase.setUp(self)
        self.filenames = []

    def tearDown(self):
        for f in self.filenames:
            if (os.path.exists(f)):
                os.remove(f)
        ApprovalsTestCase.tearDown(self)

    def test_approve_text(self):
        self.Approvals.approve("should be approved")

    def test_approve_text_with_missing_golden_master(self):
        try:
            self.Approvals.approve("should not be approved")
            self.fail("Should have raised ApprovalError")
        except ApprovalError, e:
            gm_missing = e.approval_failure.golden_master_missing
            received_file = e.approval_failure.received_filename 
            self.filenames.append(received_file)

        self.assertTrue(os.path.exists(received_file))
        self.assertTrue(gm_missing)

    def test_approve_text_with_mismatch(self):
        try:
            self.Approvals.approve("should not be approved")
            self.fail("Should have raised ApprovalError")
        except ApprovalError, e:
            gm_missing = e.approval_failure.golden_master_missing
            received_file = e.approval_failure.received_filename
            self.filenames.append(received_file)
        self.assertTrue(os.path.exists(received_file))
        self.assertFalse(gm_missing)

if __name__ == "__main__":
    unittest.main()