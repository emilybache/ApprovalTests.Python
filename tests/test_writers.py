import unittest
import os

from approvals.writers import TextWriter

class TextWriterTest(unittest.TestCase):

    def setUpe(self):
        self.cleanup()
    def tearDown(self):
        self.cleanup()
    def cleanup(self):
        to_delete = ["foo.received.txt", "foo.approved.txt"]
        for f in to_delete:
            if os.path.exists(f):
                os.remove(f)

    def test_write_a_file(self):
        writer = TextWriter("data to write")
        received = writer.write_received_file("foo")
        self.assertEquals("foo.received.txt", received)
        assert os.path.exists(received)
        with open(received) as f:
            assert "data to write" in f.read()

    def test_received_filename(self):
        self.assertEquals("foo.received.txt", TextWriter.received_filename("foo"))

    def test_approved_filename(self):
        self.assertEquals("foo.approved.txt", TextWriter.approved_filename("foo"))
