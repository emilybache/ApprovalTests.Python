
class TextWriter(object):
    def __init__(self, data):
        self.data = data

    def write_received_file(self, basename):
        filename = self.received_filename(basename)
        with open(filename, "w") as f:
            f.write(self.data)
        return filename

    @classmethod
    def received_filename(clazz, basename):
        return basename + ".received.txt"

    @classmethod
    def approved_filename(clazz, basename):
        return basename + ".approved.txt"