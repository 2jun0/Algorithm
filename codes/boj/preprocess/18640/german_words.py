import fasttext
import re
from collections import defaultdict

model = fasttext.load_model('./lid.176.ftz')

# def is_german_word(word):
#   if not re.match(r'^[a-zA-Z]+$', word):
#     return False

#   p = model.predict(word, k=1)
#   return '__label__en' in p[0]

def is_german_word(word):
  # a-zA-ZäöüÄÖÜß
  if not re.match(r'^[a-zA-ZäöüÄÖÜß]*$', word):
    return False

  p = model.predict(word, k=3)
  return '__label__de' in p[0]

german_words = []
with open('./wikinames.txt', 'r') as f:
  for word in f:
    word = word.strip('\n').strip()
    if is_german_word(word):
      german_words.append(word)

german_words = list(filter(lambda word: len(word) < 8, german_words))

tmpw = [defaultdict(int) for _ in range(100)]
for word in german_words:
  for l in range(len(word)):
    tmpw[l][word[:l]] += 1

def get_weight(word):
  w = 0
  for l in range(len(word)):
    w += tmpw[l][word[:l]] * (l+1)

  return (-w, len(word))

german_words = sorted(german_words, key=lambda word: get_weight(word))

# german_words.sort(key=lambda word: (-len(tp[word]), -len(tw[word])))
german_words = german_words[:50_000]
german_words.sort()

with open('./germanwords.txt', 'w') as f:
  f.write('\n'.join(german_words))

print('finished!')