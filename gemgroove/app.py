import os
import json
from web3 import Web3
from pathlib import Path
import streamlit as st


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
          
@st.cache(allow_output_mutation=True)
def load_contract():

          with open(Path('./contracts/compiled/music2blockchain_abi.json')) as f:
              music2blockchain_abi = json.load(f) 
          contract_address = ("0x9028D87B4F631bB28D30b7CAd377542FE2955Cc8")
          
          contract = w3.eth.contract(
              address=contract_address,
              abi=music2blockchain_abi
          )


          return contract 
contract = load_contract()         
          
st.title("Turn your song into a Music2Blockchain NFT!")
accounts = w3.eth.accounts
address = st.selectbox("Select Song Owner", options=accounts)
gemgroove_uri = st.text_input("The URI to your song - your file on IPFS")
          
if st.button("Mint my Song!"):
    tx_hash = contract.functions.registermusic2blockchain(address, music2blockchain_uri).transact({
        "from": address,
        "gas": 1000000
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
