import sys

class CommandlineReporter(object):
    def __init__(self, out = None):
        self.out = out or sys.stdout

    def report(self, failure):
        if failure.diff:
            print >> self.out, "diff %s %s" % (failure.received_filename, failure.approved_filename)
            print >> self.out, "\n%s\n" % failure.diff
        elif failure.golden_master_missing:
            print >> self.out, "Golden Master was missing."
        print >> self.out, "To approve this result:"
        print >> self.out, "mv %s %s" % (failure.received_filename, failure.approved_filename)
        
    def approved_when_reported(self):
        return False