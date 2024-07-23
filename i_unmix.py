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
    RETURN_TYPES = ("VHS_AUDIO", "VHS_AUDIO", "VHS_AUDIO",)
    RETURN_NAMES = ("drums", "vocals", "other",)

    FUNCTION = "unmix"

    def unmix(self, audio):
        # load unmix model (auto download)
        separator = umxl(targets=['drums', 'vocals', 'other'])

        # load VHS audio
        file = BytesIO(audio())
        audio, rate = torchaudio.load(file)

        print(f"audio rate: {rate}")

        # extract audio
        estimates = predict.separate(audio=audio, rate=rate, separator=separator)

        # drums
        drumsBuffer = BytesIO()
        torchaudio.save(drumsBuffer, torch.squeeze(estimates['drums']).to("cpu"), sample_rate=rate, format='wav')
        drums = lambda : drumsBuffer.getvalue()

        # vocals
        vocalsBuffer = BytesIO()
        torchaudio.save(vocalsBuffer, torch.squeeze(estimates['vocals']).to("cpu"), sample_rate=rate, format='wav')
        vocals = lambda : vocalsBuffer.getvalue()

        # other
        otherBuffer = BytesIO()
        torchaudio.save(otherBuffer, torch.squeeze(estimates['other']).to("cpu"), sample_rate=rate, format='wav')
        other = lambda : otherBuffer.getvalue()

        # return audio in VHS expected format (a lambda callback)
        return (drums, vocals, other,)

