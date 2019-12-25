from __future__ import annotations
import abc
import math
import string
from typing import ClassVar, Final, Mapping, Dict


class Cipher(abc.ABC):
    @abc.abstractmethod
    def encrypt(self, plaintext: str) -> str:
        pass

    @abc.abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        pass


# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
class VigenereCipher(Cipher):
    @staticmethod
    def _rotate(n: int) -> str:
        return string.ascii_uppercase[n:] + string.ascii_uppercase[:n]

    # https://stackoverflow.com/q/13905741/839733
    # https://docs.python.org/3/reference/executionmodel.html#resolution-of-names
    # Alternative 1: (lambda r=rotate.__func__: {chr(i + ord("A")): r(i) for i in range(26)})()
    # Alternative 2: zip(
    #   (chr(i + ord("A")) for i in range(26)),
    #   map(rotate.__func__, range(26)),
    # )
    _TABLE: Final[ClassVar[Mapping[str, str]]] = \
        {chr(i + ord("A")): r(i) for r in (_rotate.__func__,) for i in range(26)}

    def __init__(self, key: str):
        assert key, "Key must be non empty"
        self.key = key.upper()

    def _repeat_key(self, n) -> str:
        return (self.key * math.ceil(n / len(self.key)))[:n]

    def encrypt(self, plaintext: str) -> str:
        characters = zip(self._repeat_key(len(plaintext)), plaintext.upper())
        return "".join([VigenereCipher._TABLE[c1][ord(c2) - ord("A")] for c1, c2 in characters])

    def decrypt(self, ciphertext: str) -> str:
        characters = zip(self._repeat_key(len(ciphertext)), ciphertext.upper())
        return "".join([chr(VigenereCipher._TABLE[c1].index(c2) + ord("A")) for c1, c2 in characters])


# https://www.cryptomuseum.com/crypto/vernam.htm
class VernamCipher(Cipher):
    # https://www.cryptomuseum.com/crypto/baudot.htm
    _TABLE: Final[ClassVar[Dict[str, int]]] = dict({
        ("A", 0b00011),
        ("B", 0b11001),
        ("C", 0b01110),
        ("D", 0b01001),
        ("E", 0b00001),
        ("F", 0b01101),
        ("G", 0b11010),
        ("H", 0b10100),
        ("I", 0b00110),
        ("J", 0b01011),
        ("K", 0b01111),
        ("L", 0b10010),
        ("M", 0b11100),
        ("N", 0b01100),
        ("O", 0b11000),
        ("P", 0b10110),
        ("Q", 0b10111),
        ("R", 0b01010),
        ("S", 0b00101),
        ("T", 0b10000),
        ("U", 0b00111),
        ("V", 0b11110),
        ("W", 0b10011),
        ("X", 0b11101),
        ("Y", 0b10101),
        ("Z", 0b10001)
    })

    _REV_TABLE: Final[ClassVar[Mapping[str, str]]] = {v: k for k, v in _TABLE.items()}

    def __init__(self, key: str):
        assert key, "Key must be non empty"
        self.key = key.upper()

    def _repeat_key(self, n) -> str:
        return (self.key * math.ceil(n / len(self.key)))[:n]

    def _crypt(self, text: str) -> str:
        characters = zip(self._repeat_key(len(text)), text.upper())
        return "".join(map(lambda kv: VernamCipher._REV_TABLE[VernamCipher._TABLE[kv[0]] ^ VernamCipher._TABLE[kv[1]]],
                           characters))

    def encrypt(self, plaintext: str) -> str:
        return self._crypt(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self._crypt(ciphertext)


# https://en.wikipedia.org/wiki/Caesar_cipher
class CaesarCipher(Cipher):
    def __init__(self, shift: int):
        self.shift = shift

    @staticmethod
    def _crypt(text: str, shift: int) -> str:
        result = []
        for ch in text:
            if ch.isupper():
                x = (ord(ch) - ord("A") + shift) % 26
                result.append(string.ascii_uppercase[x])
            else:
                result.append(ch)

        return "".join(result)

    def encrypt(self, plaintext: str) -> str:
        return CaesarCipher._crypt(plaintext, self.shift)

    def decrypt(self, ciphertext: str) -> str:
        return CaesarCipher._crypt(ciphertext, -self.shift)
