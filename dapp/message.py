# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from contractvmd.chain import message
from . import proto

class BlockStoreMessage (message.Message):
	def set (key, value):
		m = BlockStoreMessage ()
		m.Key = key
		m.Value = value
		m.DappCode = proto.BlockStoreProto.DAPP_CODE
		m.Method = proto.BlockStoreProto.METHOD_SET
		return m

	def toJSON (self):
		data = super (BlockStoreMessage, self).toJSON ()

		if self.Method == proto.BlockStoreProto.METHOD_SET:
			data['key'] = self.Key
			data['value'] = self.Value
		else:
			return None

		return data
