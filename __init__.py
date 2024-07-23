"""
@author: Isaac Emesowum
@title: Isaac's Nodes
@nickname: Isaac's Nodes
@description: This extension offers automatic drums extraction from audio files, as well as a few helper nodes to support my audio synchronization AnimateDiff workflows.
"""

# Copyright Isaac Emesowum, 2024
"""
This file is part of ComfyUI_IsaacNodes.
ComfyUI_IsaacNodes is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
ComfyUI_IsaacNodes is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with ComfyUI_IsaacNodes. If not, see <https://www.gnu.org/licenses/>.
"""
from .i_unmix import I_UnmixAudio
from .i_amplitude import I_BinaryAmplitudeGate, I_AmplitudeToWeights
from .i_amplitude import I_WeightsListToWeights

NODE_CLASS_MAPPINGS = {
    "I_UnmixAudio": I_UnmixAudio,
    "I_BinaryAmplitudeGate": I_BinaryAmplitudeGate,
    "I_AmplitudeToWeights": I_AmplitudeToWeights,
    "I_WeightsListToWeights": I_WeightsListToWeights,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "I_UnmixAudio": "Isaac's Audio Unmixer (drums)",
    "I_BinaryAmplitudeGate": "Isaac's Binary Amplitude Gate",
    "I_AmplitudeToWeights": "Isaac's Amplitude To Weights",
    "I_WeightsListToWeights": "Isaac's Weights List to Weights",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
