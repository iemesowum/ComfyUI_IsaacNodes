# Copyright Isaac Emesowum, 2024
"""
This file is part of ComfyUI_IsaacNodes.
ComfyUI_IsaacNodes is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
ComfyUI_IsaacNodes is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with ComfyUI_IsaacNodes. If not, see <https://www.gnu.org/licenses/>.
"""
from pathlib import Path
import torchaudio
import torch
from io import BytesIO
from openunmix import umxl
from openunmix import predict

class I_UnmixAudio:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": { "audio": ("AUDIO",), },}

    CATEGORY = "Isaac's Nodes"
    RETURN_TYPES = ("AUDIO", "AUDIO", "AUDIO",)
    RETURN_NAMES = ("drums", "vocals", "other",)

    FUNCTION = "unmix"

    def unmix(self, audio):
        # load unmix model (auto download)
        separator = umxl(targets=['drums', 'vocals', 'other'])

        # load VHS audio
        rate = audio["sample_rate"]
        audio = audio["waveform"]

        print(f"audio rate: {rate}")

        # extract audio
        estimates = predict.separate(audio=audio, rate=rate, separator=separator)

        # drums
        drumsBuffer = BytesIO()
        drums = {"waveform": estimates['drums'], "sample_rate": rate}

        # vocals
        vocalsBuffer = BytesIO()
        vocals = {"waveform": estimates['vocals'], "sample_rate": rate}

        # other
        otherBuffer = BytesIO()
        other = { "waveform": estimates['other'], "sample_rate": rate }

        return (drums, vocals, other,)

