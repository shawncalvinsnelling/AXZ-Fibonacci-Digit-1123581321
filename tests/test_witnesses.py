from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WITNESSES = ROOT / "data" / "witnesses_1_to_7972.tsv"


def test_witness_file_boundary():
    lines = WITNESSES.read_text().splitlines()
    assert lines[0] == "n\texpression"
    assert len(lines) == 7973
    assert lines[-1].startswith("7972\t")


def test_stated_boundary_witness_value():
    assert 1 - ((1 + 2) * (((3 - (5 + 81)) * 32) - 1)) == 7972
