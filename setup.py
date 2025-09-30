from setuptools import setup, find_packages

setup(
    name="solana-airdrop-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "solana",
        "spl-token-py",
        "pandas",
        "openpyxl",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "solana-airdrop=airdrop.cli:main",
        ],
    },
)