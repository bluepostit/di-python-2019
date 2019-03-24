from encoder import Encoder


TEST_MESSAGE = "The quick brown fox jumps over the lazy dog"

def get_code_map(message, code):
    mapped = {}
    for (plain_letter, code_letter) in zip(message, code):
        mapped[plain_letter] = code_letter
    return mapped


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


def test_consistent_encode():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,. ' * 2
    e = Encoder()
    encoded = e.encode(letters)
    mapped = get_code_map(letters, encoded)

    for i in range(len(letters)):
        plain_letter = letters[i]
        code_letter = encoded[i]
        assert code_letter == mapped[plain_letter]


def test_encode_and_decode():
    e = Encoder()
    encoded = e.encode(TEST_MESSAGE)
    decoded = e.decode(encoded)
    assert decoded == TEST_MESSAGE
