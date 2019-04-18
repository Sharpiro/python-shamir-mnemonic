from collections import namedtuple
import shamir_mnemonic

shamir = shamir_mnemonic.ShamirMnemonic()

# groups = [(3, 5)]
# group_threshold = 1
# secret = bytes(range(16))
# mnemonics = shamir.generate_mnemonics(group_threshold, groups, secret)

# for mnemonic in mnemonics[0]:
#     print(mnemonic)

# data = (1, 2, 3, 4, 5)
# checksum = shamir.rs1024_create_checksum(data)
# isValid = shamir.rs1024_verify_checksum(data + checksum)

# assert isValid

# print(isValid)

mnemonic_str = "academic corner academic acid amuse duckling adorn network tackle swing replace pistol twin mineral aide venture element glad sniff insect replace firm hormone beard pile dough check move lily voice founder mineral solution"
MnemonicData = namedtuple(
    "MnemonicData",
    "str identifier exponent group_index group_threshold group_count index threshold value"
)

decoded = shamir.decode_mnemonic(mnemonic_str)
# MnemonicData(*decoded)
temp = MnemonicData(mnemonic_str, *decoded)
temp=3
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

# id = 99
# iteration_exponent = 0
# group_index = 0
# group_threshold = 1
# group_count = 1
# member_index = 0
# member_threshold = 3
# padded_share_value = padding + (8 * n)
# checksum = 30

# temp = shamir.encode_mnemonic(id, iteration_exponent, group_index, group_threshold, group_count,
#     member_index, member_threshold, bytes(padded_share_value))

# total_bits = (id + iteration_exponent + group_index + group_threshold + group_count +
#               member_index + member_threshold + padded_share_value + checksum)
# print("padding:", padding)
# print("share bits:", n*8)
# print("padded share:", padded_share_value)
# print("total bits:", total_bits)




