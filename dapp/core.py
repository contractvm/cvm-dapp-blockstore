# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from contractvmd import dapp, config

logger = logging.getLogger(config.APP_NAME)

class BlockStoreCore (dapp.Core):
	#def __init__ (self, chain, database):
	#	super (BlockStoreCore, self).__init__ (chain, database)

	def set (self, key, value):
		if self.database.exists (key):
			return
		else:
			self.database.set (key, value)

	def get (self, key):
		if not self.database.exists (key):
			return None
		else:
			return self.database.get (key)
