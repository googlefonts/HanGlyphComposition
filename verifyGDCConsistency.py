import pathlib


def parseDict(src):
    d = {}
    for line in src.splitlines():
        assert ":" in line, line
        k, v = line.split(":")
        assert len(k) == 1
        d[ord(k)] = {ord(c) for c in v}
    return d


root = pathlib.Path(__file__).resolve().parent

allPath = root / "GlyphsDeepComposition" / "AllDeepComponents.txt"
cg2dcPath = root / "GlyphsDeepComposition" / "Characters2DeepComponents.txt"
dc2cgPath = root / "GlyphsDeepComposition" / "DeepComponents2characters.txt"

allDC = set(ord(c) for c in allPath.read_text(encoding="utf-8"))
cg2dc = parseDict(cg2dcPath.read_text(encoding="utf-8"))
dc2cg = parseDict(dc2cgPath.read_text(encoding="utf-8"))

dc2cgKeys = set(dc2cg)

assert not dc2cgKeys - allDC
assert not allDC - dc2cgKeys

for k, v in cg2dc.items():
    for c in v:
        assert k in dc2cg[c], (k, c)

for k, v in dc2cg.items():
    for c in v:
        assert k in cg2dc[c], (k, c)
