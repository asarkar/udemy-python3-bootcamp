# asarkar:sec-14$ python -m unittest discover

from capstone.text.cipher import Cipher, VigenereCipher, VernamCipher, CaesarCipher

class TestCipher:
	def test_vigenere_cipher(self):
		cipher = VigenereCipher("LEMON")
		plaintext = "ATTACKATDAWN"
		ciphertext = cipher.encrypt(plaintext)

		assert ciphertext == "LXFOPVEFRNHR"
		assert cipher.decrypt(ciphertext) == plaintext

	def test_vernam_cipher(self):
		cipher = VernamCipher("AXHJB")
		plaintext = "HELLO"
		ciphertext = cipher.encrypt(plaintext)

		assert ciphertext == "QMIBE"
		assert cipher.decrypt(ciphertext) == plaintext

	def test_caesar_cipher(self):
		cipher = CaesarCipher(-3)
		plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
		ciphertext = cipher.encrypt(plaintext)

		assert ciphertext == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
		assert cipher.decrypt(ciphertext) == plaintext
