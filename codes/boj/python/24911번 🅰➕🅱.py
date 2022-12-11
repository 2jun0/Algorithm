import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

emojis = [
  ('🧑‍🏫', '22'),
('🧑🏻‍🏫', '22'),
('🧑🏼‍🏫', '22'),
('🧑🏽‍🏫', '22'),
('🧑🏾‍🏫', '22'),
('🧑🏿‍🏫', '22'),
('👨‍🏫', '22'),
('👨🏻‍🏫', '22'),
('👨🏼‍🏫', '22'),
('👨🏽‍🏫', '22'),
('👨🏾‍🏫', '22'),
('👨🏿‍🏫', '22'),
('👩‍🏫', '22'),
('👩🏻‍🏫', '22'),
('👩🏼‍🏫', '22'),
('👩🏽‍🏫', '22'),
('👩🏾‍🏫', '22'),
('👩🏿‍🏫', '22'),
  ('💯', '100'),
  ('🏪', '24'),
  ('🏎️', '3'),
  ('🥇', '1'),
  ('🥈', '2'),
  ('🥉', '3'),
  ('🎱', '8'),
  ('🎰', '777'),
  ('📟', '40404'),
  ('📆', '17'),
  ('📅', '17'),
  ('🔞', '18'),
  ('🔂', '1'),
  ('1️⃣', '1'),
  ('2️⃣', '2'),
  ('3️⃣', '3'),
  ('4️⃣', '4'),
  ('5️⃣', '5'),
  ('6️⃣', '6'),
  ('7️⃣', '7'),
  ('8️⃣', '8'),
  ('9️⃣', '9'),
  ('0️⃣', '0'),
  ('🔟', '10'),
  ('🔢', '1234'),
  ('', '109'),
]

def remove_skinton(s):
  skinton = ['🏻','🏼','🏽','🏾','🏿']
  
  for c in skinton:
    s = s.replace(c, '')
  return s

def emoji2num(s):
  for key, s_num in emojis:
    s = s.replace(key, s_num)
    
  return int(s)

def num2emoji(num):
  s = str(num)
  
  dp = ['']*(len(s)+1)
  cnts = [999]*(len(s)+1)
  cnts[0] = 0
  
  for i in range(len(s)):
    for key, s_num in emojis:
      srt_idx = i - len(s_num) + 1
      if srt_idx < 0:
        continue
      
      check = s[srt_idx:i+1]
      
      if check == s_num:
        if cnts[i+1] > cnts[srt_idx] + 1:
          dp[i+1] = dp[srt_idx] + key
          cnts[i+1] = cnts[srt_idx] + 1
  
  return dp[-1]

a = input()
b = input()

a = emoji2num(a)
b = emoji2num(b)

c = (a+b)
# c = 1091081881777171000022
print(num2emoji(c))