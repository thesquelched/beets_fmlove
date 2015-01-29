import importlib


def test_import():
    assert importlib.import_module('beets_fmlove') is not None
