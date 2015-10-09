# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from contractvmd import dapp, config
from . import api, core, proto, message

logger = logging.getLogger(config.APP_NAME)

class blockstore (dapp.Dapp):
	def __init__ (self, chain, db, dht, apiMaster):
		self.core = core.BlockStoreCore (chain, db)
		api = api.BlockStoreAPI (self.core, dht, apiMaster)
		super (blockstore, self).__init__("BS", proto.BlockStoreProto.DAPP_CODE, proto.BlockStoreProto.METHOD_LIST, chain, db, dht, api)

	def handleMessage (self, m):
		if m.Method == proto.BlockStoreProto.METHOD_SET:
			logger.pluginfo ('Found new message %s: set %s', m.Hash, m.Data['key'])
			self.core.set (m.Data['key'], m.Data['value'])
			
		
