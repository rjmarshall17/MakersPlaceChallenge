# -*- coding: utf-8 -*-

from web3 import Web3
# from web3.contract import Contract
from web3.middleware import geth_poa_middleware

# infura = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/e5073899fdf54bce9c2d7e173bf80ebf'))
infura = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/e5073899fdf54bce9c2d7e173bf80ebf'))

infura.middleware_onion.inject(geth_poa_middleware, layer=0)

# print(dir(infura))
block = infura.eth.getBlock(6607985)
for i,transaction in enumerate(block.transactions):
    trx = infura.eth.getTransaction(transaction)
    # if hasattr(trx,'input'):
    #     input = Contract.decode_function_input(trx.input)
    print('For transaction %d %s' % (i,transaction))
    #     print(input)
    #     print('='*20)