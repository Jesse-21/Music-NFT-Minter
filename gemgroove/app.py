import os
import json
from web3 import Web3
from pathlib import Path
import streamlit as st


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
          
@st.cache(allow_output_mutation=True)
def load_contract():

          with open(Path('./contracts/compiled/gemgroove_abi.json')) as f:
              gemgroove_abi = json.load(f) 
          contract_address = ("0xDb1CC195c06223a48A6ab8a9B258Dd3faE761684")
          
          contract = w3.eth.contract(
              address=contract_address,
              abi=gemgroove_abi
          )


          return contract 
contract = load_contract()         
          
st.title("Turn your song into a GemGroove!")
accounts = w3.eth.accounts
address = st.selectbox("Select Jam Owner", options=accounts)
gemgroove_uri = st.text_input("The URI to your Jam")
          
if st.button("Mint my Jam!"):
    tx_hash = contract.functions.registerGemGroove(address, gemgroove_uri).transact({
        "from": address,
        "gas": 1000000
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))