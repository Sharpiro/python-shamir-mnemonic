# import shamir_mnemonic

# shamir = shamir_mnemonic.ShamirMnemonic()

# groups = [(3, 5)]
# group_threshold = 1
# secret = bytes(range(16))
# mnemonics = shamir.generate_mnemonics(group_threshold, groups, secret)

# for mnemonic in mnemonics[0]:
#     print(mnemonic)

# y1 = shamir.gfMul(0, 78)

# x = 1
# shares = [
#     (0, b'\xe6\xa3\xa1H\x07\xc8\xb1\xca-\x03\xe2Y\xb8m\x97\x0f'),
#     (254, b'qg\xf8O\xe4\xd5\x84)\xc8\x00\xdc\xae\xdcC\x1e\xe2'),
#     (255, b'\xf8\x8a\xda\xe4$5\xa6\xf67E7s(\x8b\x02\xca')]

# print(list(shares[0][1]))
# print(list(shares[1][1]))
# print(list(shares[2][1]))
# print(list(b"oN\x83\xe3\xc7(\x93\x15\xd2F\t\x84L\xa5\x8b'"))

# expected = list(b"oN\x83\xe3\xc7(\x93\x15\xd2F\t\x84L\xa5\x8b'")
# actual = list(shamir._interpolate(shares, x))

# result = expected == actual
# print(result)


# def ghetto_polate(shares, x):
#     pass

# n = 16
# padding = 10 - (n*8) % 10

# id = 15
# iteration_exponent = 5
# group_index = 4
# group_threshold = 4
# group_count = 4
# member_index = 4
# member_threshold = 4
# padded_share_value = padding + (8 * n)
# checksum = 30

# total_bits = (id + iteration_exponent + group_index + group_threshold + group_count +
#               member_index + member_threshold + padded_share_value + checksum)
# print("padding:", padding)
# print("share bits:", n*8)
# print("padded share:", padded_share_value)
# print("total bits:", total_bits)


'''
0111 // 7
0101 // 5
1110 // carry
1100 // result = 12
'''


'''
10001 // 17
00101 // 5
00010 // carry
10110 // result = 22
'''


def add_bin(x, y):
    carry = 0
    sum = ""
    sum_temp = 0
    z = 0
    for i in range(9):
        two_power = 1 << i
        x_i = (x & two_power) >> i
        y_i = (y & two_power) >> i
        sum_i_carry = x_i ^ y_i ^ carry

        if (sum_i_carry == 1):
            z = z ^ two_power
        else:
            temp = 2
        # print("x_i:", x_i)
        # print("y_i:", y_i)
        # print("carry:", carry)
        # print("sum_i:", sum_i)
        # print("sum_i_carry:", sum_i_carry)
        # print("---------------")
        sum += str(sum_i_carry)
        # sum_temp = sum_temp << 1
        # if (sum_i_carry == 1):
        #     sum_temp = sum_temp | 1
        # update
        # carry = x_i | y_i | carry
        carry = (x_i & y_i) | (x_i & carry) | (y_i & carry)
        # if x_i and y_i equal 1
        # or x_i and carry equal 1
        # or y_i and carry equal 1
        # x >>= 1
        # y >>= 1

    # if (carry == 1):
        # sum_temp = sum_temp << sum_i_carry
        # sum_temp  = sum_temp | 1
        # sum += str(carry)

    # sum_temp = sum_temp << carry
    # sum_temp = sum_temp | carry
    # z = z << carry
    # z = z | carry

    return (sum, sum_temp, z)


x = 12
y = 5
z = (bin(x+y)[2:], x + y)
# print(bin(x)[2:])
# print(bin(y)[2:])
# print(z)
# (print(x + y), 99)
# print(add_bin(x, y))


for i in range(255):
    for j in range(255):
        bin_res = add_bin(i, j)[2]
        norm_res = i + j
        assert bin_res == norm_res
        print(i, j)
