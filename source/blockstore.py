# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from .. import config, dapp
from ..proto import Protocol
from ..chain.message import Message

logger = logging.getLogger(config.APP_NAME)

class BlockStoreDapp (dapp.Dapp):
	def __init__ (self, chain, db, dht, apiMaster):
		self.core = BlockStoreCore (chain, db)
		api = BlockStoreAPI (self.core, dht, apiMaster)
		super (BlockStoreDapp, self).__init__("BS", BlockStoreProto.DAPP_CODE, BlockStoreProto.METHOD_LIST, chain, db, dht, api)

	def handleMessage (self, m):
		if m.Method == BlockStoreProto.METHOD_SET:
			logger.pluginfo ('Found new message %s: set %s', m.Hash, m.Data['key'])
			self.core.set (m.Data['key'], m.Data['value'])
			
		
