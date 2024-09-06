#ifndef HASHFUNCTION_H
#define HASHFUNCTION_H

#include <string.h>
#include <stdint.h>
#include "BlockProcessor.h"
#include "BitManipulator.h"

#define HASH_SIZE 32  // Output hash size in bytes (256 bits)

// HashFunction class that implements the cryptographic hash function
class HashFunction {
private:
    uint8_t hash[HASH_SIZE]; // Stores the final hash

public:
    HashFunction() {
        memset(hash, 0, HASH_SIZE);  // Initialize hash to zero
    }

    // Hashes the input message and returns the hash
    void hashMessage(const uint8_t* message, size_t len) {
        // Step 1: Padding the message to make it a multiple of block size
        size_t padded_len = BitManipulator::padMessage(message, len);
        
        // Step 2: Initialize hash values (we can use predefined constants, similar to SHA-256)
        uint32_t hash_values[8] = { 0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                                    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19 };

        // Step 3: Process the message in blocks
        BlockProcessor::processBlocks(message, padded_len, hash_values);

        // Step 4: Convert final hash values into byte array
        BitManipulator::toByteArray(hash_values, hash, HASH_SIZE);
    }

    // Returns the final hash as a byte array
    const uint8_t* getHash() const {
        return hash;
    }

    // Prints the hash in hexadecimal format
    void printHash() const {
        for (int i = 0; i < HASH_SIZE; i++) {
            printf("%02x", hash[i]);
        }
        printf("\n");
    }
};

#endif
