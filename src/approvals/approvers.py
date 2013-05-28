import os
import difflib

from failures import ApprovalFailure

class FileApprover(object):
    def __init__(self, writer, namer):
        self.writer = writer
        self.namer = namer
        self.failure = None
    
    def approve(self):
        basename = os.path.join(self.namer.source_file_path, self.namer.approval_name)
        golden_master = self.writer.approved_filename(basename)
        
        if not os.path.exists(golden_master):
            self.writer.write_received_file(basename)
            self.failure = ApprovalFailure(self.writer.received_filename(basename), 
                                           golden_master, 
                                           golden_master_missing=True)
            return False
        
        with open(golden_master) as gm:
            if self.has_received_identical(gm):
                return True
            else:
                self.writer.write_received_file(basename)
                self.failure = ApprovalFailure(self.writer.received_filename(basename),
                                               golden_master, 
                                               golden_master_missing=False, 
                                               diff=self.diff)
                return False

    def has_received_identical(self, golden_master):
        self.diff = file_diff(golden_master.readlines(), self.writer.data.splitlines())
        return not self.diff

def file_diff(gm, rec):
    return list(difflib.unified_diff(gm, rec))
        