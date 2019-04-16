from hypothesis import given, settings, example
from hypothesis import strategies as st

@given(st.text())
@example('ß')
@settings(max_examples=2000)
def test_decode_inverts_encode(s):
    assert s.upper().lower() == s.lower()

