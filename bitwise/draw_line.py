from nose.tools import assert_equal

all_ones = (1 << 8) - 1


def print_binary(x):
    print('{0:08b}'.format(x))


class BitsScreen(object):

    def set_last_n_bits(self, row, n):
        mask = (1 << n) - 1
        return all_ones & (row | mask)

    def set_first_n_bits(self, row, n):
        mask = ~(1 << (8 - n))
        return all_ones & ~(row | mask)

    def set_all_bits(self, row):
        return all_ones | row

    def draw_line(self, screen, width, x1, x2):
        x1_row = x1 // 8
        x2_row = x2 // 8
        if x1_row != x2_row:
            screen[x1_row] = self.set_last_n_bits(
                screen[x1_row], 8 - (x1 % 8))
            screen[x2_row] = self.set_first_n_bits(
                screen[x2_row], x2 % 8 + 1)
        for i in range(x1_row + 1, x2_row):
            screen[i] = all_ones | screen[i]


class TestBitsScreen(object):

    def test_draw_line(self):
        bits_screen = BitsScreen()
        screen = []
        for _ in range(20):
            screen.append(int('00000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=68, x2=80)
        for row in screen:
            print_binary(row)
        assert_equal(screen[8], int('00001111', base=2))
        assert_equal(screen[9], int('11111111', base=2))
        assert_equal(screen[10], int('10000000', base=2))

        bits_screen.draw_line(screen, width=32, x1=2, x2=6)
        assert_equal(screen[0], int('00111110', base=2))
        bits_screen.draw_line(screen, width=32, x1=10, x2=13)
        assert_equal(screen[1], int('00111100', base=2))
        print('Success: test_draw_line')


def main():
    test = TestBitsScreen()
    test.test_draw_line()


if __name__ == '__main__':
    main()
