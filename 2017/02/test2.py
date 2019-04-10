#!/usr/bin/env python3
import unittest
import challenge1

class TestChallenge1(unittest.TestCase):
    def test1(self):
        self.assertEqual(challenge1.captcha("1122"), 3)

    def test2(self):
        self.assertEqual(challenge1.captcha("1111"), 4)

    def test3(self):
        self.assertEqual(challenge1.captcha("1234"), 0)

    def test4(self):
        self.assertEqual(challenge1.captcha("91212129"), 9)

if __name__ == '__main__':
    unittest.main()