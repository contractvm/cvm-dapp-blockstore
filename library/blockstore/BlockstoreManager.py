# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, ConsensusManager, DappManager

class BlockstoreManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (BlockstoreManager, self).__init__(consensusManager, wallet)

	def set (self, key, value):
		cid = self._produce_transaction ('blockstore.set', [key, value])
		return cid
	
	def get (self, key):
		return self.consensusManager.jsonConsensusCall ('blockstore.get', [key])['result']
