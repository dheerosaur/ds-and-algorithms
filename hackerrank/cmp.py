import collections


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    counter = collections.Counter()
    for size in range(1, len(s)):
        for i in range(len(s) - size + 1):
            key = ''.join(sorted(s[i:i+size]))
            counter[key] += 1
    return sum((s * (s - 1) // 2) for s in counter.values())


def main():
    cases = [
        'abba',
        'ifailuhkqq',
        'kkkk',
        'cdcd',
    ]
    for case in cases:
        print(sherlockAndAnagrams(case))


if __name__ == '__main__':
    main()
