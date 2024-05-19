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
        return {"required": { "audio": ("VHS_AUDIO",), },}

    CATEGORY = "Isaac's Nodes"
    RETURN_TYPES = ("VHS_AUDIO",)
    RETURN_NAMES = ("audio",)

    FUNCTION = "unmix"

    def unmix(self, audio):
        # load unmix model (auto download)
        separator = umxl(targets=['drums', 'other'])

        # load VHS audio
        file = BytesIO(audio())
        audio, rate = torchaudio.load(file)

        # extract audio
        estimates = predict.separate(audio=audio, rate=rate, separator=separator)
        buffer = BytesIO()
        torchaudio.save(buffer, torch.squeeze(estimates['drums']).to("cpu"), sample_rate=rate, format='wav')
        # return audio in VHS expected format (a lambda callback)
        audio = lambda : buffer.getvalue()
        return (audio,)

