# Solana Token Airdrop CLI


A Python command-line tool for airdropping SPL tokens on Solana using CSV/XLSX spreadsheets.


---


## Features
- Import recipients and amounts from **CSV/XLSX** files.
- **Mint tokens** (requires mint authority) OR **transfer tokens** from payer's token account.
- Automatic **ATA (Associated Token Account)** creation.
- **Multithreaded** for faster distribution.
- **Dry-run** mode for testing without sending transactions.
- Logs results to JSON file.


---


## Install


```bash
# Clone the repo
git clone https://github.com/yourusername/solana-airdrop-cli.git
cd solana-airdrop-cli


# Create a virtual environment
python3 -m venv venv
source venv/bin/activate


# Install dependencies
pip install -r requirements.txt
```


---


## Usage


### Mint Tokens (requires mint authority)
```bash
python -m airdrop.cli \
--rpc https://api.devnet.solana.com \
--keypair ./payer-keypair.json \
--mint <TOKEN_MINT> \
--csv recipients.csv \
--amount-col amount \
--address-col address \
--decimals 6 \
--mint-authority \
--concurrency 10
```


### Transfer Tokens (from payer’s ATA)
```bash
python -m airdrop.cli \
--rpc https://api.devnet.solana.com \
--keypair ./payer-keypair.json \
--mint <TOKEN_MINT> \
--csv recipients.csv \
--amount-col amount \
--address-col address \
--decimals 6 \
--concurrency 5
```


### Dry Run
```bash
python -m airdrop.cli --rpc https://api.devnet.solana.com \
--keypair ./payer-keypair.json --mint <TOKEN_MINT> \
--csv recipients.csv --dry-run
```


---


## Spreadsheet Format


CSV/XLSX with headers:
```csv
address,amount
Fv...1,10.5
Dp...2,1
```


---


## License
MIT
