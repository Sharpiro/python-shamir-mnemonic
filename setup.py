import os.path

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="shamir-mnemonic",
    version="0.0.1",
    description="SLIP-39 Shamir Mnemonics",
    long_description=long_description,
    url="https://github.com/trezor/python-shamir-mnemonic",
    author="Satoshi Labs",
    packages=["shamir_mnemonic"],
    python_requires=">=3.6",
    install_requires=["click>=7,<8", "colorama"],
    package_data={"shamir_mnemonic": ["wordlist.txt"]},
    entry_points={"console_scripts": ["shamir=shamir_mnemonic.cli:cli"]},
)
