#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, WalletNode, ConsensusManager
from blockstore import BlockstoreManager
import sys
import config

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")
#consMan.addNode ("http://127.0.0.1:2819")
#consMan.addNode ("http://127.0.0.1:2820")

#wallet=WalletChainSo.WalletChainSo (wallet_file='data/test_xltnode_a.wallet')
wallet=WalletNode.WalletNode (chain='XLT', url=config.WALLET_NODE_URL, wallet_file='data/test_xltnode_a.wallet')

bsMan = BlockstoreManager.BlockstoreManager (consMan, wallet=wallet)

def set_key ():
	ykey = input ('Insert a key to set: ')
	yvalue = input ('Insert a value to set: ')
	try:
		bsMan.set (ykey, yvalue)
	except:
		print ('Error.')

def get_key ():
	ykey = input ('Insert a key to get: ')
	value = bsMan.get (ykey)
	print (ykey,'=',value)


if __name__ == "__main__":
	if len (sys.argv) > 1:
		if sys.argv[1] == 'set':
			set_key ()
			sys.exit (0)

		elif sys.argv[1] == 'get':
			get_key ()
			sys.exit (0)

	print ('usage:', sys.argv[0], 'get|set')
