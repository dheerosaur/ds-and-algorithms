def odd_even(n):
    odd_bits = (0b10101010 & n) >> 1
    even_bits = (0b01010101 & n) << 1
    return odd_bits | even_bits
