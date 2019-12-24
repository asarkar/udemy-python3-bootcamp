from __future__ import annotations
from enum import Enum, auto
import abc
import string
from typing import ClassVar, Dict
import math

class Cipher(abc.ABC):
	@abc.abstractmethod
	def encrypt(self, plaintext: str) -> str:
		pass

	@abc.abstractmethod
	def decrypt(self, ciphertext: str) -> str:
		pass

def rotate(n: int) -> str:
	return string.ascii_uppercase[n:] + string.ascii_uppercase[:n]

# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
class VigenereCipher(Cipher):
	__TABLE: ClassVar[Dict[str, str]] = dict({(chr(i + ord("A")), rotate(i)) for i in range(26)})

	def __init__(self, key: str):
		assert key, "Key must be non empty"
		self.key = key.upper()

	def __repeat_key(self, n) -> str:
		return (self.key * math.ceil(n / len(self.key)))[:n]

	def encrypt(self, plaintext: str) -> str:
		characters = zip(self.__repeat_key(len(plaintext)), plaintext.upper())
		return "".join([VigenereCipher.__TABLE[c1][ord(c2) - ord("A")] for c1, c2 in characters])

	def decrypt(self, ciphertext: str) -> str:
		characters = zip(self.__repeat_key(len(ciphertext)), ciphertext.upper())
		return "".join([chr(VigenereCipher.__TABLE[c1].index(c2) + ord("A")) for c1, c2 in characters])

# https://www.cryptomuseum.com/crypto/vernam.htm
class VernamCipher(Cipher):
	# https://www.cryptomuseum.com/crypto/baudot.htm
	__TABLE: ClassVar[Dict[str, int]] = dict({
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

	__REV_TABLE: ClassVar[Dict[str, str]] = {v: k for k, v in __TABLE.items()}

	def __init__(self, key: str):
		assert key, "Key must be non empty"
		self.key = key.upper()

	def __repeat_key(self, n) -> str:
		return (self.key * math.ceil(n / len(self.key)))[:n]

	def __crypt(self, text: str) -> str:
		characters = zip(self.__repeat_key(len(text)), text.upper())
		return "".join(map(lambda kv: VernamCipher.__REV_TABLE[VernamCipher.__TABLE[kv[0]] ^ VernamCipher.__TABLE[kv[1]]], characters))

	def encrypt(self, plaintext: str) -> str:
		return self.__crypt(plaintext)

	def decrypt(self, ciphertext: str) -> str:
		return self.__crypt(ciphertext)

# https://en.wikipedia.org/wiki/Caesar_cipher
class CaesarCipher(Cipher):
	def __init__(self, shift: int):
		self.shift = shift

	def __crypt(self, text: str, shift: int) -> str:
		result = []
		for ch in text:
			if (ch.isupper()):
				x = (ord(ch) - ord("A") + shift) % 26
				result.append(string.ascii_uppercase[x])
			else:
				result.append(ch)

		return "".join(result)

	def encrypt(self, plaintext: str) -> str:
		return self.__crypt(plaintext, self.shift)

	def decrypt(self, ciphertext: str) -> str:
		return self.__crypt(ciphertext, -self.shift)
