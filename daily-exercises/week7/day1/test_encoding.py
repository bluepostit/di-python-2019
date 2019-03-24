from encoder import Encoder


TEST_MESSAGE = "The quick brown fox jumps over the lazy dog"


def test_constructor():
    e = Encoder()
    assert isinstance(e, Encoder)


def test_encode():
    e = Encoder()
    encoded = e.encode(TEST_MESSAGE)
    assert len(encoded) == len(TEST_MESSAGE)
    assert encoded != TEST_MESSAGE


def test_decode():
    e = Encoder()
    decoded = e.decode(TEST_MESSAGE)
    assert len(decoded) == len(TEST_MESSAGE)
    assert decoded != TEST_MESSAGE


def test_encode_and_decode():
    e = Encoder()
    encoded = e.encode(TEST_MESSAGE)
    decoded = e.decode(encoded)
    assert decoded == TEST_MESSAGE
    