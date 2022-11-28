import lzma
import base64
import os 

_end = '_'

def make_trie(words):
  root = dict()
  for word in words:
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = _end
  return root

german_words = []
with open('./germanwords.txt', 'r') as f:
  german_words = [s.strip('\n') for s in f.readlines()]

trie = make_trie(german_words)

string = str(trie).replace(' ', '').replace('\'', '')#.replace(':', '').replace('{}', '')

# string = ','.join(german_words)
compressed = base64.b85encode(lzma.compress(string.encode()))

with open('./compressed.txt', 'wb') as f:
  f.write(compressed)

fbytes = os.path.getsize('./compressed.txt')
print('compressed file size : ' + str(fbytes) + 'B')

print('finished!')