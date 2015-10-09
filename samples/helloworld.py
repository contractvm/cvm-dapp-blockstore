#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, WalletNode, BlockStoreManager, ConsensusManager
import sys
import config

consMan = ConsensusManager.ConsensusManager ()
consMan.addNode ("http://127.0.0.1:8181")
#consMan.addNode ("http://127.0.0.1:2819")
#consMan.addNode ("http://127.0.0.1:2820")

wallet=WalletNode.WalletNode (chain='XLT', url=config.WALLET_NODE_URL, wallet_file='data/test_xltnode_a.wallet')
			
bsMan = BlockStoreManager.BlockStoreManager (consMan, wallet=wallet)

def set_key ():
	ykey = input ('Insert a key to set: ')
	yvalue = input ('Insert a value to set: ')
	bsMan.set (ykey, yvalue)
	
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
