from itertools import groupby

from .espeak_config import espeak_conf, espeak_conf_low


def _classify(x):
    if not x.isalpha():
        return None
    if x.islower():
        return "lower"
    return "upper"


def split_by_case(text):
    CONF = {"upper": espeak_conf_low, "lower": espeak_conf}

    gb = []
    for k, v in groupby(text, _classify):
        v = "".join(v)
        if k == "upper" and len(v) < 2:
            k = "lower"
        gb.append((k, v))

    new_gb = []
    for i, (k, v) in enumerate(gb):
        if k is None:
            if i > 0 and gb[i - 1][0] == "lower":
                k = "lower"
            elif i < len(gb) - 1 and gb[i + 1][0] == "lower":
                k = "lower"
            else:
                k = "upper"
        new_gb.append((k, v))

    gb = groupby(new_gb, lambda x: x[0])

    result = []
    for k, v in gb:
        k = CONF[k]
        v = "".join(x[1] for x in v)
        result.append((v, k))
    return result


def default(text):
    return [(text, espeak_conf)]
