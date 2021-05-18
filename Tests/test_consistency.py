import pathlib


def parseDict(src):
    d = {}
    for lineno, line in enumerate(src.splitlines(), 1):
        assert ":" in line, line
        k, v = line.split(":")
        assert k.strip(), (lineno, line)
        # if "." in k:
        #     assert len(k.split(".")[0]) == 1
        # else:
        #     assert len(k) == 1
        if "." in v:
            d[k] = {c for c in v.split()}
        else:
            d[k] = set(v.strip().replace(" ", ""))
    return d


repoRoot = pathlib.Path(__file__).resolve().parent.parent

alldcPath = repoRoot / "GlyphsDeepComposition" / "AllDeepComponents.txt"
cg2dcPath = repoRoot / "GlyphsDeepComposition" / "Characters2DeepComponents.txt"
dc2cgPath = repoRoot / "GlyphsDeepComposition" / "DeepComponents2characters.txt"

alldc = set(alldcPath.read_text(encoding="utf-8").split())
cg2dc = parseDict(cg2dcPath.read_text(encoding="utf-8"))
dc2cg = parseDict(dc2cgPath.read_text(encoding="utf-8"))


def test_matching_keys():
    assert set(dc2cg) == alldc


def test_cg2dc_to_dc2cg_consistency():
    for k, v in cg2dc.items():
        for c in v:
            if not k in dc2cg[c]:
                print(dc2cg[c])
            assert k in dc2cg[c], (k, c)


def test_dc2cg_to_cg2dc_consistency():
    for k, v in dc2cg.items():
        for c in v:
            assert k in cg2dc[c], (k, c)
