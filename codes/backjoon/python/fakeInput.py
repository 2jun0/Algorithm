class InputLoader:
  def __init__(self):
    pass
  def next_input_line(self):
    pass

class FileInputLoader(InputLoader):
  def __init__(self, path:str):
    super().__init__()

    self.fp = open(path, 'r')

  def next_input_line(self):
    return self.fp.readline()

loader = None
def set_input_loader(_loader:InputLoader):
	global loader
	loader = _loader

def set_input_file(path:str):
	global loader
	loader = FileInputLoader(path)

def fake_input(func):
  def _input(_type=str):
	  return _type(loader.next_input_line())
  return _input

"""
## fake input
from fakeInput import fake_input, set_input_file
set_input_file('./1006번 습격자 초라기.txt')
@fake_input
## fake input
"""