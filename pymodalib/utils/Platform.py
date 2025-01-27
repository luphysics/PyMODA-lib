#  PyMODAlib, a Python implementation of the algorithms from MODA (Multiscale Oscillatory Dynamics Analysis).
#  Copyright (C) 2020 Lancaster University
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
import platform
from enum import Enum


class Platform(Enum):
    LINUX = "Linux"
    WINDOWS = "Windows"
    MAC_OS = "macOS"

    @staticmethod
    def get() -> "Platform":
        system = platform.system()

        if system == "Windows":
            return Platform.WINDOWS
        elif system == "Linux":
            return Platform.LINUX
        else:
            return Platform.MAC_OS
