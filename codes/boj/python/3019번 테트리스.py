import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


class Block:
    def __init__(self, shape):
        self.shape = self._preprocess_shape(shape)
        self.min_ys = self._shape_min_ys()

    def rotate_cw(self) -> "Block":
        # (1,0), (0,1) -> (0,-1), (1,0)
        new_shape = []
        for y, x in self.shape:
            new_x = y
            new_y = -x
            new_shape.append((new_y, new_x))

        return Block(new_shape)

    def can_fill(self, map: list[int], x: int) -> bool:
        for offset in range(self.witdh):
            map_diff = map[x] - map[x + offset]
            block_diff = self.min_ys[0] - self.min_ys[offset]
            if map_diff != block_diff:
                return False

        return True

    def _shape_min_ys(self) -> list[int]:
        max_x = max(x for _, x in self.shape)
        min_ys = [100] * (max_x + 1)

        for y, x in self.shape:
            min_ys[x] = min(min_ys[x], y)

        return min_ys

    @classmethod
    def _preprocess_shape(cls, shape: list[int]) -> list[int]:
        min_x = min(x for _, x in shape)
        min_y = min(y for y, _ in shape)

        new_shape = []
        for y, x in shape:
            new_shape.append((y - min_y, x - min_x))

        return new_shape

    @property
    def witdh(self):
        return len(self.min_ys)


blocks = [
    Block(shape=[(0, 0), (1, 0), (2, 0), (3, 0)]),
    Block(shape=[(0, 0), (1, 0), (0, 1), (1, 1)]),
    Block(shape=[(0, 0), (0, 1), (1, 1), (1, 2)]),
    Block(shape=[(0, 1), (0, 2), (1, 0), (1, 1)]),
    Block(shape=[(0, 0), (0, 1), (0, 2), (1, 1)]),
    Block(shape=[(0, 0), (0, 1), (0, 2), (1, 2)]),
    Block(shape=[(0, 0), (0, 1), (0, 2), (1, 0)]),
]

max_rotate_cnt = [1, 0, 1, 1, 3, 3, 3]

C, P = input_n(int)
A = input_n(int)

block = blocks[P - 1]
r_cnt = max_rotate_cnt[P - 1]
rs = 0

for _ in range(r_cnt + 1):
    for x in range(len(A) - block.witdh + 1):
        if block.can_fill(A, x):
            rs += 1
    block = block.rotate_cw()

print(rs)
