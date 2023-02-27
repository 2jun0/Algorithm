import re
import os
import sys
import unittest
from datetime import datetime

dir_path = sys.argv[1]

problem_filename_pattern = r'^(\d+)번'

def is_problem_filename(filename):
  return re.match(problem_filename_pattern, filename)

def parse_problem_number(filename):
  match = re.search(problem_filename_pattern, filename)
  return match.group(1)

def get_modification_time(filename):
  file_path = f'{dir_path}/{filename}'
  m_time = os.path.getmtime(file_path)
  return datetime.fromtimestamp(m_time)

class DuplicatedProblemFileNamesException(Exception):
  class Log:
    def __init__(self, pnumber, filenames):
      self.pnumber = pnumber
      self.filenames = filenames
    
    def __str__(self):
      msgs = [f'Duplicated Filename - number: {self.pnumber}']
      for filename in self.filenames:
        mdt = get_modification_time(filename)
        msgs.append(f'filename : {repr(filename)}, {mdt}')
        
      return '\n'.join(msgs)
  
  def __init__(self, logs: list[Log]):
    self.logs = logs
  
  def __str__(self):
    return '\n----------------------------------------------------------------------\n'.join(map(str, self.logs))

class TestDuplicatedProblems(unittest.TestCase):
  problems = []
  pnum2filenames = dict()
  
  @classmethod
  def setUpClass(cls):
    filenames = os.listdir(dir_path)
    
    for filename in filenames:
      if is_problem_filename(filename):
        cls.problems.append(filename)
        
    for filename in cls.problems:
      if is_problem_filename(filename):
        pnum = parse_problem_number(filename)
        cls.pnum2filenames.setdefault(pnum, []).append(filename)
  
  def test_duplicated_filenames(self):
    logs = []
    for pnumber, filenames in self.pnum2filenames.items():
      if len(filenames) > 1:
        logs.append(DuplicatedProblemFileNamesException.Log(pnumber, filenames))
        
    if logs:
      raise DuplicatedProblemFileNamesException(logs)

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'])