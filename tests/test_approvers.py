import unittest
import os
from mockito import *

from approvals.namers import SimpleNamer
from approvals.writers import TextWriter
from approvals.approvers import FileApprover, file_diff

class FileApproverTest(unittest.TestCase):
    
    def setUp(self):
        self.cleanup()
    def tearDown(self):
        self.cleanup()
    def cleanup(self):
        to_delete = ["foo.received.txt", "foo.approved.txt"]
        for f in to_delete:
            if os.path.exists(f):
                os.remove(f)

    def test_missing_golden_master(self):
        writer = TextWriter("file contents")
        namer = SimpleNamer("foo", os.getcwd())
        approver = FileApprover(writer, namer)
        self.assertFalse(approver.approve())
        self.assertTrue(os.path.exists("foo.received.txt"))
        self.assertIsNotNone(approver.failure)

    def test_file_diff(self):
        gm = ["file contents"]
        rec = "file contents".splitlines()
        self.assertEquals([], file_diff(gm, rec))

    def test_approve_passing(self):
        writer = TextWriter("file contents")
        namer = SimpleNamer("foo", os.getcwd())
        approver = FileApprover(writer, namer)
        with open("foo.approved.txt", "w") as f:
            f.write("file contents")
        self.assertTrue(approver.approve())
        self.assertFalse(os.path.exists("foo.received.txt"))

    def test_approve_with_a_diff(self):
        writer = TextWriter("file contents")
        namer = SimpleNamer("foo", os.getcwd())
        approver = FileApprover(writer, namer)
        with open("foo.approved.txt", "w") as f:
            f.write("file contents changed")
        self.assertFalse(approver.approve())
        self.assertTrue(os.path.exists("foo.received.txt"))
        self.assertIsNotNone(approver.failure)
