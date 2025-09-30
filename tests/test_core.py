import pytest
from solana.keypair import Keypair
from solana.publickey import PublicKey
from airdrop.core import Airdropper

# Dummy test just to validate structure
def test_to_amount_raw():
    kp = Keypair()
    a = Airdropper("https://api.devnet.solana.com", kp, PublicKey(kp.public_key), 6, dry_run=True)
    assert a.to_amount_raw(1.23) == 1230000
