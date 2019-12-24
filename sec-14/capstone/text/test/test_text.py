import capstone.text.functions as text


class TestText:
    def test_rev(self):
        assert text.rev("abc") == "cba"

    def test_pig_latin(self):
        assert text.pig_latin("pig") == "igpay"
        assert text.pig_latin("eat") == "eatay"

    def test_count_vowels(self):
        assert text.count_vowels("smile") == {"i": 1, "e": 1}
        assert not text.count_vowels("x")

    def test_is_palindrome(self):
        assert text.is_palindrome("racecar")
        assert text.is_palindrome("abba")
        assert not text.is_palindrome("abc")
