import configparser
from pathlib import Path

from deepwick_spec.check_port import check_port
from deepwick_spec.palette import ANSI_KEYS, load_palette

REPO = Path(__file__).resolve().parents[1]
PALETTE = load_palette()
C = PALETTE.colors
KNOWN_KEYS = {
    "Name", "Background", "Foreground", "Cursor",
    "SuperuserBackground", "SuperuserForeground", "RemoteBackground", "RemoteForeground",
    *(f"Color{i}" for i in range(16)),
}


def palette_section():
    parser = configparser.ConfigParser(interpolation=None)
    parser.optionxform = str
    parser.read(REPO / "deepwick.palette", encoding="utf-8")
    assert parser.sections() == ["Palette"]
    return parser["Palette"]


def test_name():
    assert palette_section()["Name"] == "Deepwick"


def test_terminal_colors_follow_spec_terminal_roles():
    p = palette_section()
    t = PALETTE.terminal
    assert p["Background"] == C[t["background"]]
    assert p["Foreground"] == C[t["foreground"]]
    assert p["Cursor"] == C[t["cursor"]]


def test_ansi_16_in_slot_order():
    p = palette_section()
    assert [p[f"Color{i}"] for i in range(16)] == [PALETTE.ansi[k] for k in ANSI_KEYS]


def test_header_bar_colors():
    p = palette_section()
    assert (p["SuperuserBackground"], p["SuperuserForeground"]) == (C["red"], C["background"])
    assert (p["RemoteBackground"], p["RemoteForeground"]) == (C["magenta"], C["background"])


def test_only_keys_ptyxis_reads():
    assert set(palette_section()) <= KNOWN_KEYS


def test_port_conventions():
    assert check_port(REPO, PALETTE.allowed_hex()) == []
