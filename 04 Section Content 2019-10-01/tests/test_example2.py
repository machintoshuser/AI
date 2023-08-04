# Example 2: for cryptography - why should we write unit tests?

"""
Fernet Encryption is a type of symmetric encryption, where only one key is used to encrypt and decrypt the same information.

This example briefly touches on cryptography, which might be useful to some people. Here is a good usecase of why we might want to add some tests - we want to make sure we can decrypt what we encrypt!

* Might take a bit too long to cover, especially b/c context needs to be given
"""
import unittest
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EncryptionTest(unittest.TestCase):
    def setUp(self):
        password = (
            b"password"
        )  # come up with a password that forms the basis of encryption
        kdf = PBKDF2HMAC(
            # this is an encryption algorithm. We can slow down rainbow attacks by a key derivation function.
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(16),
            iterations=100000,
            backend=default_backend(),
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))
        self.f = Fernet(key)
        self.token = self.f.encrypt(b"Secret message!")

    def testEncryptDecrypt(self):
        self.assertEqual(
            self.f.decrypt(self.token), b"Secret message!"
        )  # let's test that you can successfully decrypt!

    def testKeys(self):
        password = b"password"  # redefine the password

        kdf1 = PBKDF2HMAC(  # recompute the
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(16),
            iterations=100000,
            backend=default_backend(),
        )

        key1 = base64.urlsafe_b64encode(kdf1.derive(password))
        f1 = Fernet(key1)

        self.assertNotEqual(
            self.f, key1
        )  # we know that the encryption objects are not the same

    def tearDown(self):
        del self.f
        del self.token


# what other tests could we implement?
