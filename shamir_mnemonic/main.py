import shamir_mnemonic

shamir = shamir_mnemonic.ShamirMnemonic()

groups = [(2, 5)]
threshold = 1
secret = bytes(range(16))
mnemonics = shamir.generate_mnemonics(threshold, groups, secret)

for mnemonic in mnemonics[0]:
    print(mnemonic)
