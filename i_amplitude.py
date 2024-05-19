# Copyright Isaac Emesowum, 2024
"""
This file is part of ComfyUI_IsaacNodes.
ComfyUI_IsaacNodes is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
ComfyUI_IsaacNodes is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with ComfyUI_IsaacNodes. If not, see <https://www.gnu.org/licenses/>.
"""
import numpy as np

class I_BinaryAmplitudeGate:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "normalized_amp": ("NORMALIZED_AMPLITUDE",),
            "threshold": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 1.0, "step": 0.01}),
        }}
    CATEGORY = "Isaac's Nodes"
    RETURN_TYPES = ("NORMALIZED_AMPLITUDE",)
    RETURN_NAMES = ("normalized_amp",)
    FUNCTION = "gate"

    def gate(self, normalized_amp, threshold: float):
        binary_amp = np.where(normalized_amp > threshold, 1.0, 0.0)
        return (binary_amp,)

class I_WeightsListToWeights:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "weights_list": ("FLOAT", {}),
        }}
    CATEGORY = "Isaac's Nodes"
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("weights",)
    FUNCTION = "execute"

    def execute(self, weights_list,):
        return (weights_list[0],)

