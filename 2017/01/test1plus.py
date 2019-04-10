#!/usr/bin/env python3
import unittest
import challenge1plus

class TestChallenge1Plus(unittest.TestCase):
    def test1(self):
        self.assertEqual(challenge1plus.captcha("1212"), 6)

    def test2(self):
        self.assertEqual(challenge1plus.captcha("1221"), 0)

    def test3(self):
        self.assertEqual(challenge1plus.captcha("123425"), 4)

    def test4(self):
        self.assertEqual(challenge1plus.captcha("123123"), 12)

    def test5(self):
        self.assertEqual(challenge1plus.captcha("12131415"), 4)

if __name__ == '__main__':
    unittest.main()