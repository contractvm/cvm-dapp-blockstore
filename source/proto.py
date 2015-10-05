# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from ..proto import Protocol

class BlockStoreProto:
	DAPP_CODE = 0x08
	METHOD_SET = 0x01
	METHOD_LIST = [METHOD_SET]
