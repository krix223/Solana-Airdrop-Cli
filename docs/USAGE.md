# Usage Guide

### Spreadsheet format
```csv
address,amount
Fv..1,100
Dp..2,50
```

### Mint mode
```bash
solana-airdrop --rpc https://api.devnet.solana.com \
--keypair ./payer.json --mint <TOKEN_MINT> \
--csv recipients.csv --mint-authority
```

### Transfer mode
```bash
solana-airdrop --rpc https://api.devnet.solana.com \
--keypair ./payer.json --mint <TOKEN_MINT> \
--csv recipients.csv
```

### Dry run
```bash
solana-airdrop --rpc https://api.devnet.solana.com \
--keypair ./payer.json --mint <TOKEN_MINT> \
--csv recipients.csv --dry-run
```