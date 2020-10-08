from reader_file import read
import random
class Random(object):
    """docstring for Random."""

    def __init__(self):
        super(Random, self).__init__()
        self.set = []

    def load_file(self, path, attach=False):
        if not attach:
            self.set = []
        file_content = read(path)
        format_content = file_content.split('\n')
        while True:
            try:
                format_content.remove('')
            except Exception as e:
                break
        for number in format_content:
            try:
                self.set.append(float(number.replace(',','.')))
            except Exception as e:
                continue

    def load(self, max=100, limit_float=None, attach=False):
        if not attach:
            self.set = []
        for i in range(max):
            number = random.random() if limit_float == None else round(random.random(), limit_float)
            self.set.append(number)

    def congruencial_generator(self, a, m, c=0, x0=1, max=100, limit_float=None):
        pass
