#  Drakkar-Software trading-backend
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
VERSION = "1.0.16"
PROJECT_NAME = "trading-backend"

from trading_backend import exchange_factory
from trading_backend.exchange_factory import (
    create_exchange_backend,
    is_sponsoring,
)
from trading_backend import errors
from trading_backend.errors import (
    TimeSyncError,
    ExchangeAuthError,
)

__all__ = [
    "create_exchange_backend",
    "is_sponsoring",
    "TimeSyncError",
    "ExchangeAuthError",
]
