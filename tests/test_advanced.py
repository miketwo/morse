# -*- coding: utf-8 -*-

import morse
import pytest


# Parameterized testing. Change the test cases to generate more.
@pytest.mark.parametrize("input_string, expected", [
    ("abc 123", ".- -... -.-.|.---- ..--- ...--"),
    ("AbC 123", ".- -... -.-.|.---- ..--- ...--"),
    ("   AbC 123   ", ".- -... -.-.|.---- ..--- ...--"),
    ("Hey, not a bad implementation", ".... . -.--|-. --- -|.-|-... .- -..|.. -- .--. .-.. . -- . -. - .- - .. --- -.")
])
def test_encode(input_string, expected):
    assert morse.translate.encode(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    (".- -... -.-.|.---- ..--- ...--", "ABC 123"),
    (".... . -.--|-. --- -|.-|-... .- -..|.. -- .--. .-.. . -- . -. - .- - .. --- -.", "HEY NOT A BAD IMPLEMENTATION")
])
def test_decode(input_string, expected):
    assert morse.translate.decode(input_string) == expected
