import re


def snakecase(s: str) -> str:
    s = re.sub(r"[\-\.\s]", "", s)
    return s[0].lower() + re.sub(
        r"[A-Z]", lambda matched: "_" + (matched.group(0)).lower(), s[1:]
    )


def snakecase2(s):
    return "_".join(
        re.sub(
            "([A-Z][a-z]+)", r" \1", re.sub(r"([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


with open("/proc/cpuinfo") as f:
    for line in f:
        parameter = line.split(":")[0]
        # print(parameter)
        print("self." + snakecase2(parameter))
