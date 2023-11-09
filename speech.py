#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from openai import OpenAI

client = OpenAI()

text = \
    """
    西北カリキア地方の天気予報をお送りします。
    大陸より張り出した高気圧によって、
    天気は次第に回復に向かっています。
    今夕は、西北西の風、風力は3、晴れ。
    素晴らしい満月の夜になるでしょう。
    あしたは晴れでしょう。
    あさっては晴れでしょう。
    """

voices = ["alloy","echo","fable","onyx","nova","shimmer"]

for basename in voices:

    filename = os.path.join("mp3", basename + ".mp3")

    if os.path.exists(filename):
        print("exist:", filename)
        continue
        
    print(filename)


    response = client.audio.speech.create(
        model = "tts-1",
        voice = basename,
        input = text
    )

    response.stream_to_file(filename)
    
# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
