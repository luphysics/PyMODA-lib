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
"""
Imports useful functions to make them easily accessible.
"""

from pymodalib.algorithms.harmonics import harmonicfinder
from pymodalib.algorithms.preprocessing import preprocess
from pymodalib.algorithms.signals import resampl_flow as downsample
from pymodalib.algorithms.wavelet import wavelet_transform
from pymodalib.algorithms.coherence import wphcoh, tlphcoh
from pymodalib.algorithms.group_coherence import group_coherence, dual_group_coherence
from pymodalib.utils.cache import cachedarray, cleanup

# Make these functions accessile with different names.
wavelet_phase_coherence = wphcoh
time_localised_wavelet_phase_coherence = tlphcoh

# This isn't important; it just ensures that PyCharm doesn't try to remove unnecessary imports.
__imported = (
    cachedarray,
    cleanup,
    group_coherence,
    dual_group_coherence,
    downsample,
    preprocess,
    wavelet_transform,
    harmonicfinder,
)
