# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
from ..chain.message import Message

class BlockStoreMessage (Message):
	def set (key, value):
		m = BlockStoreMessage ()
		m.Key = key
		m.Value = value
		m.PluginCode = BlockStoreProto.DAPP_CODE
		m.Method = BlockStoreProto.METHOD_SET
		return m

	def toJSON (self):
		data = super (BlockStoreMessage, self).toJSON ()

		if self.Method == BlockStoreProto.METHOD_SET:
			data['key'] = self.Key
			data['value'] = self.Value
		else:
			return None

		return data
