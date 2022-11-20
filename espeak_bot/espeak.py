import shlex
import subprocess

import unidecode

from .strategy import split_by_case


def preprocess_text(text):
    text = unidecode.unidecode(text)
    text = text + " "  # preserve "dot" pronunciation if last char
    return text


def voice_with_config(text, espeak_conf):
    text = preprocess_text(text)
    return subprocess.run(["espeak", *espeak_conf, "--stdout", shlex.quote(text)], capture_output=True).stdout


def voice(text, strategy=split_by_case):
    chunks = strategy(text)
    return b"".join(voice_with_config(*args) for args in chunks)
