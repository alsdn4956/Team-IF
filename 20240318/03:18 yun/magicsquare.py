class MagicSquare:
    def __init__(self, size):
        self.size = size
        self.mat = [[0 for _ in range(size)] for _ in range(size)]
    def move_coexter(self, row, col):
        """coexter rules"""
        r, c = row - 1, col - 1
        r = self.size - 1 if r < 0 else r
        c = self.size - 1 if c < 0 else c
        if self.mat[r][c]:
            r, c = row + 1, col
        return r, c
    def build(self):
        """build matrix"""
        count, COUNT = 1, self.size * self.size
        r, c = 0, self.size // 2
        self.mat[r][c] = count
        while count < COUNT:
            r, c = self.move_coexter(r, c)
            count += 1
            self.mat[r][c] = count

    def __str__(self):
        ret = ""
        for r in range(self.size):
            for c in range(self.size):
                ret += f"%2d " % self.mat[r][c]
            ret += "\n"
        return ret.strip()
    
def main():
    SIZE = 7
    ms = MagicSquare(SIZE)
    ms.build()
    print(ms)

if __name__ == "__main__":
    main()
