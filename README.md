```

██╗    ██╗ █████╗ ██╗  ██╗███████╗    
██║    ██║██╔══██╗██║  ██║██╔════╝    
██║ █╗ ██║███████║███████║███████╗    
██║███╗██║██╔══██║██╔══██║╚════██║    
╚███╔███╝ ██║  ██║██║  ██║███████║    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    
  WHAT THE HASH - Hash Identifier    

```

> *Because staring at 32 hex chars isn't a strategy.*


## Installation

```bash
git clone https://github.com/yourusername/WhatTheHash.git
cd WhatTheHash
```

## Usage

### Basic Usage

```bash
python whatthehash.py -s 5d41402abc4b2a76b9719d911017c592
```

### With Different Flags

```bash
# Using --hash instead of -s
python whatthehash.py --hash 356a192b7913b04c54574d18c28d46e6395428ab

# Don't display banner
python whatthehash.py -s 5d41402abc4b2a76b9719d911017c592 --no-banner
```

### Help

```bash
python whatthehash.py --help
```

## Supported Hash Types

### Generic Hashes
- CRC32, MD4, MD5, NTLM, RipeMD-128, Haval-128, Tiger-128
- MySQL323, DES (Unix)
- SHA1, RipeMD-160, Tiger-160, Haval-160
- MySQL5
- SHA224, Haval-192, Tiger-192
- SHA256, Haval-224
- SHA384, SHA512
- Whirlpool, GOST

### Salted/Modern Password Hashes
- Bcrypt
- MD5crypt, SHA256crypt, SHA512crypt
- BSDi Extended DES
- Scrypt
- Argon2
- PBKDF2

## Examples

### Identify an MD5 hash
```bash
$ python whatthehash.py -s 5d41402abc4b2a76b9719d911017c592

============================================================
Hash Input: 5d41402abc4b2a76b9719d911017c592
Hash Length: 32 characters
============================================================

Possible hash types:
  - MD4
  - MD5
  - NTLM
  - RipeMD-128
  - Haval-128
  - Tiger-128
```

### Identify a SHA1 hash
```bash
$ python whatthehash.py -s 356a192b7913b04c54574d18c28d46e6395428ab

Possible hash types:
  - SHA1
  - RipeMD-160
  - Tiger-160
  - Haval-160
```

### Identify a Bcrypt hash
```bash
$ python whatthehash.py -s '$2b$12$eImiTXuWVxfaHNYY0iNAseK2kIrt8E8/65cuT0jVmYGEunDvHvG3m'

Possible hash types:
  - Bcrypt
```
