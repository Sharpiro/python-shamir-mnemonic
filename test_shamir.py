import json

import pytest

from shamir_mnemonic.shamir_mnemonic import MnemonicError, ShamirMnemonic

MS = b"ABCDEFGHIJKLMNOP"
shamir = ShamirMnemonic()


def test_basic_sharing_random():
    mnemonics = shamir.generate_mnemonics_random(1, [(3, 5)])[0]
    assert shamir.combine_mnemonics(mnemonics) == shamir.combine_mnemonics(
        mnemonics[1:4]
    )


def test_basic_sharing_fixed():
    mnemonics = shamir.generate_mnemonics(1, [(3, 5)], MS)[0]
    assert MS == shamir.combine_mnemonics(mnemonics)
    assert MS == shamir.combine_mnemonics(mnemonics[1:4])
    with pytest.raises(MnemonicError):
        shamir.combine_mnemonics(mnemonics[1:3])


def test_passphrase():
    mnemonics = shamir.generate_mnemonics(1, [(3, 5)], MS, b"TREZOR")[0]
    assert MS == shamir.combine_mnemonics(mnemonics[1:4], b"TREZOR")
    assert MS != shamir.combine_mnemonics(mnemonics[1:4])


def test_iteration_exponent():
    mnemonics = shamir.generate_mnemonics(1, [(3, 5)], MS, b"TREZOR", 1)[0]
    assert MS == shamir.combine_mnemonics(mnemonics[1:4], b"TREZOR")
    assert MS != shamir.combine_mnemonics(mnemonics[1:4])

    mnemonics = shamir.generate_mnemonics(1, [(3, 5)], MS, b"TREZOR", 2)[0]
    assert MS == shamir.combine_mnemonics(mnemonics[1:4], b"TREZOR")
    assert MS != shamir.combine_mnemonics(mnemonics[1:4])


def test_group_sharing():
    mnemonics = shamir.generate_mnemonics(2, [(3, 5), (2, 3), (2, 5), (1, 1)], MS)

    # All mnemonics.
    assert MS == shamir.combine_mnemonics(
        [mnemonic for group in mnemonics for mnemonic in group]
    )

    # Minimal sets of mnemonics.
    assert MS == shamir.combine_mnemonics(
        [mnemonics[2][0], mnemonics[2][2], mnemonics[3][0]]
    )
    assert MS == shamir.combine_mnemonics(
        [mnemonics[2][3], mnemonics[3][0], mnemonics[2][4]]
    )

    # Two complete groups and one incomplete group.
    assert MS == shamir.combine_mnemonics(
        mnemonics[0] + [mnemonics[1][1]] + mnemonics[2]
    )
    assert MS == shamir.combine_mnemonics(
        mnemonics[0][1:4] + mnemonics[1][1:3] + mnemonics[2][2:4]
    )

    # One complete group and one incomplete group out of two groups required.
    with pytest.raises(MnemonicError):
        shamir.combine_mnemonics(mnemonics[0][2:] + [mnemonics[1][0]])

    # One group of two required.
    with pytest.raises(MnemonicError):
        shamir.combine_mnemonics(mnemonics[0][1:4])


def test_vectors():
    with open("vectors.json", "r") as f:
        vectors = json.load(f)
    for mnemonics, secret in vectors:
        if secret:
            assert bytes.fromhex(secret) == shamir.combine_mnemonics(
                mnemonics, b"TREZOR"
            )
        else:
            with pytest.raises(MnemonicError):
                shamir.combine_mnemonics(mnemonics)
