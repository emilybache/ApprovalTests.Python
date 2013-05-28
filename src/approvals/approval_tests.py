
import writers
import approvers
import namers
import reporters
import failures

class Approvals(object):
    
    def __init__(self, namer):
        self.namer = namer
        self.reporter = reporters.CommandlineReporter()
    
    def approve(self, data):
        self.approve_with_writer(writers.TextWriter(data))
    
    def approve_with_writer(self, writer):
        approver = approvers.FileApprover(writer, self.namer)
        if not approver.approve():
            self.reporter.report(approver.failure)
            if not self.reporter.approved_when_reported():
                raise failures.ApprovalError(approver.failure)
        
