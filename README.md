How my solution meets CIA
Confidentiality - I encrypt the users data using a symmetric encryption. This hides the plaintext from anyone who does not have the key
Integrity - I compare the hash of the original data to the hash after decryption to ensure no changes have been made to the data
Availability - The program is simple and handles user input errors, preventing crashes. 

Entropy and key generation
I use Fernet.generate_key() to ensure that the key is unpredictable.
Fernet also ensures that encrypting the same data twice would generate different cypers preventing patterns from forming. 
This ensures high entropy.
