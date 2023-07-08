import sys
from enum import Enum

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

DEBUG = False
def debug(l):
  if DEBUG:
    print(l)

PLAYER = '@'
EMPTY = '.'
WALL = '#'
CHEST = 'B'
TRAP = '^'
MONSTER = '&'
BOSS = 'M'

WEAPON = 'W'
ARMOR = 'A'
ACCESSORIE = 'O'

HP_REGENERATION = 'HR'
REINCARNATION = 'RE'
COURAGE = 'CO'
EXPERIENCE = 'EX'
DEXTERITY = 'EX'
DEXTERITY = 'DX'
HUNTER = 'HU'
CURSED = 'CU'

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'
dy = {UP: -1, DOWN: 1, LEFT: 0, RIGHT: 0}
dx = {UP: 0, DOWN: 0, LEFT: -1, RIGHT: 1}

class State(Enum):
  POST_BATTLE_WIN = 'PBW'
  POST_BATTLE_LOSE = 'PBL'

## Monster

class Monster:
  def __init__(self, y: int, x: int, name: str, strike: int, defense: int, hp: int, exp: int, is_boss: bool):
    self.y = y
    self.x = x
    self.name = name
    self._std_strike = strike
    self._std_defense = defense
    self._hp_limit = hp
    self.strike = strike
    self.defense = defense
    self.hp = hp
    self.exp = exp
    self.is_boss = is_boss
    
  def heal(self, v):
    '''체력 회복'''
    assert v >= 0
    self.hp = min(self.hp + v, self._hp_limit)
    
  def attacked(self, v):
    '''공격 받기'''
    assert v >= 0
    if v == 0:
      return
    
    lose = max(1, v - self.defense)
    self.hp = max(0, self.hp - lose)
    
  def attack(self, player: 'Player', turn: int):
    '''한번 공격'''
    player.attacked(self.strike)
    
  def post_attack(self, player: 'Player', turn: int):
    self.strike = self._std_strike
    self.defense = self._std_defense
  
  def __str__(self) -> str:
    if self.is_boss:
      return BOSS
    else:
      return MONSTER
  
## Monster - end
## Player

class Player:
  def __init__(self, y, x):
    self._init_x = x
    self._init_y = y
    
    self.y = y
    self.x = x
    self.hp = 20
    self.strike = 0
    self.defense = 0
    self._hp_limit = 20
    self._std_strike = 2
    self._std_defense = 2
    self.lv = 1
    self.exp = 0
    
    self.weapon = None
    self.armor = None
    self.accessories: list[Accessorie] = []
    
  def can_lv_up(self):
    '''레벨 업을 할 수 있는가?'''
    return self.exp >= 5*self.lv
  
  def lv_up(self):
    '''레벨 업'''
    assert self.can_lv_up()
    self.lv += 1
    self.exp = 0
    self._hp_limit += 5
    self._std_strike += 2
    self._std_defense += 2
    self.hp = self._hp_limit
    
    debug(f'lv up : {self.lv-1} -> {self.lv}')
    
  def heal(self, v):
    '''체력 회복'''
    assert v >= 0
    self.hp = min(self.hp + v, self._hp_limit)
    
  def attacked(self, v):
    '''공격 받기'''
    assert v >= 0
    if v == 0:
      return
    
    lose = max(1, v - self.defense)
    self.hp = max(0, self.hp - lose)
    
  def attack(self, other: Monster, turn: int):
    '''한번 공격'''
    other.attacked(self.strike)
    
  def pre_battle(self, other: Monster):
    '''전투 전'''
    for a in self.accessories:
      a.pre_battle(self, other)
    
  def post_battle(self, other: Monster, state: State):
    '''전투 후'''
    for a in self.accessories:
      a.post_battle(self, other, state)
      
    if state == State.POST_BATTLE_WIN:
      self.exp += other.exp
      debug(f'Win : game exp = {other.exp}, total = {player.exp}/{player.lv*5}')
      if self.can_lv_up():
        self.lv_up()
  
  def pre_attack(self, other: Monster, turn: int):
    '''공격 전'''
    self.strike = self._std_strike
    self.defense = self._std_defense
    
    if self.weapon:
      self.strike += self.weapon
    if self.armor:
      self.defense += self.armor
      
    for a in self.accessories:
      a.pre_attack(self, other, turn)
    
  def post_attack(self, other: Monster, turn: int):
    '''공격 후'''
    for a in self.accessories:
      a.post_attact(self, other, turn)
      
  def post_move(self):
    '''움직인 후'''
    for a in self.accessories:
      a.post_move(self)
    
  def reset_pos(self):
    '''초기 위치로 되돌리기'''
    self.y = self._init_y
    self.x = self._init_x
  
  def add_accessorie(self, accessorie: 'Accessorie'):
    '''악세서리 추가
    최대 4개까지 착용할 수 있으나
    동일한 효과의 장신구는 최대 하나까지만 착용 가능하다
    - Return : 착용 여부
    '''
    if len(self.accessories) >= 4:
      return False
    
    for a in self.accessories:
      if a.__class__ == accessorie.__class__:
        return False
      
    self.accessories.append(accessorie)
    return True
  
  # ....
  def have_accessorie(self, cls):
    '''Deprecated'''
    for a in self.accessories:
      if isinstance(a, cls):
        return True
    return False

## Player - end
## Accessorie

class Accessorie():
  def pre_battle(self, player: Player, other: Monster):
    pass
  
  def post_battle(self, player: Player, other: Monster, state: State):
    pass
  
  def pre_attack(self, player: Player, other: Monster, turn: int):
    pass
  
  def post_attact(self, player: Player, other: Monster, turn: int):
    pass
  
  def post_move(self, player: Player):
    pass
  
class HpRegeneration(Accessorie):
  '''
  전투에서 승리할 때마다 체력을 3 회복한다. 
  체력은 최대 체력 수치까지만 회복된다.
  '''
  def post_battle(self, player: Player, other: Monster, state: State):
    if state == State.POST_BATTLE_WIN:
      player.heal(3)
      
class Reincarnation(Accessorie):
  '''
  주인공이 사망했을 때 소멸하며, 
  주인공을 최대 체력으로 부활시켜 준 뒤, 주인공을 첫 시작 위치로 돌려보낸다.
  전투 중이던 몬스터가 있다면 해당 몬스터의 체력도 최대치로 회복된다.
  '''
  def post_battle(self, player: Player, other: Monster, state: State):
    if state == State.POST_BATTLE_LOSE:
      # 주인공이 사망했을 때 소멸하며, 
      player.accessories.remove(self)
      # 주인공을 최대 체력으로 부활시켜 준 뒤, 주인공을 첫 시작 위치로 돌려보낸다.
      player.heal(player._hp_limit)
      player.reset_pos()
      # 전투 중이던 몬스터가 있다면 해당 몬스터의 체력도 최대치로 회복된다.
      other.heal(other._hp_limit)
      
      debug('Reincarnation 사용')
    
  def post_move(self, player: Player):
    if player.hp <= 0:
      # 주인공이 사망했을 때 소멸하며, 
      player.accessories.remove(self)
      # 주인공을 최대 체력으로 부활시켜 준 뒤, 주인공을 첫 시작 위치로 돌려보낸다.
      player.heal(player._hp_limit)
      player.reset_pos()
      
      debug('Reincarnation 사용')
       
class Courage(Accessorie):
  '''
  모든 전투에서, 첫 번째 공격에서 주인공의 공격력(무기 합산)이 두 배로 적용된다.
  즉, 모든 첫 공격에서 몬스터에게 max(1, 공격력×2 – 몬스터의 방어력)만큼의 데미지를 입힌다.
  '''
  def pre_attack(self, player: Player, other: Monster, turn: int):
    if turn == 0:
      if player.have_accessorie(Dexterity):
        player.strike *= 3
      else:
        player.strike *= 2
      
class Experience(Accessorie):
  '''
  얻는 경험치가 1.2배가 된다. 소수점 아래는 버린다.
  '''
  def post_battle(self, player: Player, other: Monster, state: State):
    other.exp = int(other.exp * 1.2)
  
class Dexterity(Accessorie):
  '''
  가시 함정에 입는 데미지가 1로 고정되며, 
  Courage 장신구와 함께 착용할 경우, 
  Courage의 공격력 효과가 두 배로 적용되는 대신 세 배로 적용된다.
  '''
  pass
  
class Hunter(Accessorie):
  '''
  보스 몬스터와 전투에 돌입하는 순간 체력을 최대치까지 회복하고, 
  보스 몬스터의 첫 공격에 0의 데미지를 입는다.
  '''
  def pre_battle(self, player: Player, other: Monster):
    if other.is_boss:
      player.heal(player._hp_limit)
  
  def post_attact(self, player: Player, other: Monster, turn: int):
    if other.is_boss and turn == 0:
      other.strike = 0

class Cursed(Accessorie):
  '''
  아무 능력이 없으며, 그냥 장신구 한 자리를 차지한다.
  '''
  pass

## Accessorie - end
## Chest

class Chest:
  def __init__(self, y, x):
    self.y = y
    self.x = x
  
  def open(self, player: Player):
    table[self.y][self.x] = EMPTY
    
  def __str__(self) -> str:
    return CHEST

class WeaponChest(Chest):
  def __init__(self, y, x, v):
    super().__init__(y, x)
    self.v = v
  
  def open(self, player: Player):
    super().open(player)
    player.weapon = self.v
    
class ArmorChest(Chest):
  def __init__(self, y, x, v):
    super().__init__(y, x)
    self.v = v
  
  def open(self, player: Player):
    super().open(player)
    player.armor = self.v
    
class AccessorieChest(Chest):
  def __init__(self, y, x, a: Accessorie):
    super().__init__(y, x)
    self.a = a
    
  def open(self, player: Player):
    super().open(player)
    player.add_accessorie(self.a)

## Chest - end
## Others

def battle(player: Player, monster: Monster):
  player.pre_battle(monster)
  
  turn = 0
  while player.hp > 0 and monster.hp > 0:
    player.pre_attack(monster, turn)
    player.attack(monster, turn)
    player.post_attack(monster, turn)
    
    if monster.hp <= 0:
      break
    
    monster.attack(player, turn)
    monster.post_attack(player, turn)
    turn += 1
  
  debug(f'전투 vs {m.name}, hp : {player.hp}/{player._hp_limit}')
  
  if player.hp <= 0:
    player.post_battle(monster, State.POST_BATTLE_LOSE)
  elif monster.hp <= 0:
    table[monster.y][monster.x] = EMPTY
    player.post_battle(monster, State.POST_BATTLE_WIN)

## Others - end

N, M = input_n(int)
# map
table = [list(map(str,input())) for _ in range(N)]
K, L = 0, 0
player = None
for y in range(N):
  for x in range(M):
    if table[y][x] in [BOSS, MONSTER]:
      K += 1
    if table[y][x] == CHEST:
      L += 1
    if table[y][x] == PLAYER:
      player = Player(y,x)
      table[y][x] = EMPTY
cmds = input()
# monster
for _ in range(K):
  _R, _C, S, W, A, H, E = input_n()
  R, C = int(_R)-1, int(_C)-1
  W, A, H, E = list(map(int, [W,A,H,E]))
  table[R][C] = Monster(R, C, S, W, A, H, E, table[R][C] == BOSS)
# chest
for _ in range(L):
  _R, _C, T, S = input_n()
  R, C = int(_R)-1, int(_C)-1
  if T == WEAPON:
    table[R][C] = WeaponChest(R, C, int(S))
  elif T == ARMOR:
    table[R][C] = ArmorChest(R, C, int(S))
  elif T == ACCESSORIE:
    a = None
    if S == HP_REGENERATION:
      a = HpRegeneration()
    elif S == REINCARNATION:
      a = Reincarnation()
    elif S == COURAGE:
      a = Courage()
    elif S == EXPERIENCE:
      a = Experience()
    elif S == DEXTERITY:
      a = Dexterity()
    elif S == HUNTER:
      a = Hunter()
    elif S == CURSED:
      a = Cursed()
    table[R][C] = AccessorieChest(R, C, a)

turn = 1
end_flag = 0
lastest_name = ''
for cmd in cmds:
  y, x = player.y, player.x
  ny, nx = dy[cmd]+y , dx[cmd]+x
  if 0<=ny<N and 0<=nx<M and table[ny][nx] != WALL:
    player.y = ny
    player.x = nx
    
    debug(f'- 이동 : ({ny}, {nx})')
    
    if isinstance(table[ny][nx], Chest):
      c: Chest = table[ny][nx]
      c.open(player)
    
    if isinstance(table[ny][nx], Monster):
      m: Monster = table[ny][nx]
      lastest_name = m.name
      battle(player, m)
      
      debug(f'전투 vs {m.name}, 남은 hp : {player.hp}')
      if m.is_boss and m.hp <= 0:
        end_flag = 1
        break
      
  if table[player.y][player.x] == TRAP:
    lastest_name = 'SPIKE TRAP'
    
    if player.have_accessorie(Dexterity):
      player.hp -= 1
    else:
      player.hp -= 5
    
    debug(f'가시 밟음, 남은 hp : {player.hp}')
      
  player.post_move()
      
  if player.hp <= 0:
    end_flag = 2
    break
    
  turn += 1
  
if end_flag == 0:
  turn -= 1
  
if end_flag != 2:
  table[player.y][player.x] = PLAYER
for line in table:
  print(''.join(list(map(str, line))))
print(f'Passed Turns : {turn}')
print(f'LV : {player.lv}')
print(f'HP : {player.hp}/{player._hp_limit}')
if player.weapon: print(f'ATT : {player._std_strike}+{player.weapon}')
else: print(f'ATT : {player._std_strike}+0')
if player.armor: print(f'DEF : {player._std_defense}+{player.armor}')
else: print(f'DEF : {player._std_defense}+0')
print(f'EXP : {player.exp}/{player.lv*5}')

if end_flag == 0:
  print('Press any key to continue.')
if end_flag == 1:
  print('YOU WIN!')
if end_flag == 2:
  print(f'YOU HAVE BEEN KILLED BY {lastest_name}..')
