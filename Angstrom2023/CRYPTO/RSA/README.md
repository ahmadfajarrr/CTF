We import necessary functions from the Crypto.Util.number module and the math module.

The program starts by defining the values of n, e, and c. These values are obtained from the given ciphertext, where n is the product of two large primes p and q, e is the public exponent, and c is the encrypted message.

Two variables h1 and h2 are defined with given values. These values correspond to (p-1)*(q-2) and (p-2)*(q-1) respectively.

Next, the program calculates a and b using the given formulas. These are intermediate values that will help us find the prime factors p and q.

To find the prime factors p and q, the program uses the math.gcd function (greatest common divisor) from the math module. It calculates p as gcd(b - a, n). We already know that n = p * q, so by finding p, we can easily obtain q by dividing n by p.

After obtaining p and q, we calculate the private exponent d using the inverse function from the Crypto.Util.number module. The private exponent is used to decrypt the ciphertext using the RSA decryption algorithm.

Finally, the program decrypts the ciphertext c using the private exponent d and modulus n with the pow function. The decrypted message is then converted from the long integer format to a string using the long_to_bytes function and printed as the decrypted_message.
