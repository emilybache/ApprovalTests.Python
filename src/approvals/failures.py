
class ApprovalFailure(object):
    def __init__(self, received_filename, approved_filename, golden_master_missing = False, diff=None):
        self.received_filename = received_filename
        self.approved_filename = approved_filename
        self.golden_master_missing = golden_master_missing
        self.diff = diff

class ApprovalError(Exception):
    def __init__(self, approval_failure):
        self.approval_failure = approval_failure
        self.received_filename = approval_failure.received_filename
        self.approved_filename = approval_failure.approved_filename