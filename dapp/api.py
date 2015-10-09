# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from contractvm import dapp, config
from . import message

logger = logging.getLogger(config.APP_NAME)

class BlockStoreAPI (dapp.API):
	def __init__ (self, core, dht, api):
		self.api = api
		rpcmethods = {}

		rpcmethods["get"] = {
			"call": self.method_get,
			"help": {"args": ["key"], "return": {}}
		}

		rpcmethods["set"] = {
			"call": self.method_set,
			"help": {"args": ["key", "value"], "return": {}}
		}

		errors = { 'KEY_ALREADY_SET': {'code': -2, 'message': 'Key already set'}, 'KEY_IS_NOT_SET': {'code': -3, 'message': 'Key is not set'} }


		super (BlockStoreAPI, self).__init__(core, dht, rpcmethods, errors)


	def method_get (self, key):
		v = self.core.get (key)
		if v == None:
			return self.createErrorResponse ('KEY_IS_NOT_SET')
		else:
			return v
		
	def method_set (self, key, value):
		if self.core.get (key) != None:
			return self.createErrorResponse ('KEY_ALREADY_SET')
		
		message = message.BlockStoreMessage.set (key, value)
		[datahash, outscript, tempid] = message.toOutputScript (self.dht)
		r = { "outscript": outscript, "datahash": datahash, "tempid": tempid, "fee": Protocol.estimateFee (self.core.getChainCode (), 100 * len (value)) }
		return r
