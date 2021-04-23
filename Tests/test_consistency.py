import pathlib


def parseDict(src):
    d = {}
    for line in src.splitlines():
        assert ":" in line, line
        k, v = line.split(":")
        assert len(k) == 1
        d[ord(k)] = {ord(c) for c in v}
    return d


repoRoot = pathlib.Path(__file__).resolve().parent.parent

allPath = repoRoot / "GlyphsDeepComposition" / "AllDeepComponents.txt"
cg2dcPath = repoRoot / "GlyphsDeepComposition" / "Characters2DeepComponents.txt"
dc2cgPath = repoRoot / "GlyphsDeepComposition" / "DeepComponents2characters.txt"

alldc = set(ord(c) for c in allPath.read_text(encoding="utf-8"))
cg2dc = parseDict(cg2dcPath.read_text(encoding="utf-8"))
dc2cg = parseDict(dc2cgPath.read_text(encoding="utf-8"))


def test_matching_keys():
    assert set(dc2cg) == alldc


def test_cg2dc_to_dc2cg_consistency():
    for k, v in cg2dc.items():
        for c in v:
            assert k in dc2cg[c], (k, c)


def test_dc2cg_to_cg2dc_consistency():
    for k, v in dc2cg.items():
        for c in v:
            assert k in cg2dc[c], (k, c)
