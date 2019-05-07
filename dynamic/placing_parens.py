from nose.tools import assert_equal


def place_parens2(exp):
    subs = [exp[i:i+2] for i in range(0, len(exp), 2)]
    table1 = [float('-inf')] * len(subs)
    table1[0] = eval(subs[0])
    table1[1] = eval(subs[0] + subs[1])

    for i in range(2, len(subs)):
        prev, curr = subs[i - 1], subs[i]
        ev1 = eval('{}{}'.format(table1[i - 1], curr))
        ev2 = eval('{}{}'.format(table1[i - 2], prev[0]) +
                   '({}{})'.format(prev[1], curr))
        table1[i] = max(ev1, ev2)
    return table1


def place_parens2(exp):
    # maximum of
    # exp[:-4]|exp[-4]|exp[-3:]
    # exp[:-2]|exp[-2:]


class Test:

    def test_place_parens(self, f):
        # assert_equal(f('+5*6'), 30)
        f('+1+2-3*4-5')
        f('+1+2+3+4+5')
        f('+1+2*3+4+5')
        # assert_equal(f('+1+2-3*4-5'), 6)
        print('Success: {}'.format(f.__name__))


def main():
    test = Test()
    test.test_place_parens(place_parens)


if __name__ == '__main__':
    main()
