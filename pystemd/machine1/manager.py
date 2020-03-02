#!/usr/bin/env python3
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree.
#

from typing import Optional

from pystemd.base import SDObject
from pystemd.dbuslib import DBus


class Manager(SDObject):
    def __init__(self, bus: Optional[DBus] = None, _autoload: bool = False) -> None:
        super(Manager, self).__init__(
            destination=b"org.freedesktop.machine1",
            path=b"/org/freedesktop/machine1",
            bus=bus,
            _autoload=_autoload,
        )
