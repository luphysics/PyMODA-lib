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
import numpy as np

from algorithms.harmonics.harmonics import harmonicfinder


def test_harmonics():
    time = 100
    freq = 1 / 7

    fs = 50

    times = np.arange(1 / fs, time + 1 / fs, 1 / fs)
    signal = (
        0.1 * np.random.randn(1, len(times)) + np.sin(2 * np.pi * freq * times) ** 3
    )

    scale_min = 0.5
    scale_max = 40
    sigma = 1.05
    time_res = 0.1

    output, scale_freq = harmonicfinder(
        signal, fs, scale_min, scale_max, sigma, time_res, 100
    )


if __name__ == "__main__":
    test_harmonics()
