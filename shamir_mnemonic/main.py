import shamir_mnemonic

shamir = shamir_mnemonic.ShamirMnemonic()

groups = [(3, 5)]
group_threshold = 1
secret = bytes(range(16))
mnemonics = shamir.generate_mnemonics(group_threshold, groups, secret)

for mnemonic in mnemonics[0]:
    print(mnemonic)
