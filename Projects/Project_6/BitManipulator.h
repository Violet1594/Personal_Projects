#ifndef BITMANIPULATOR_H
#define BITMANIPULATOR_H

#include <stdint.h>
#include <string.h>

class BitManipulator {
public:
    // Pads the message according to cryptographic standards (like Merkle-Damgård)
    static size_t padMessage(const uint8_t* message, size_t len) {
        size_t padded_len = len + 1;  // Add 1 byte for padding (initial 0x80 byte)
        
        // Add enough space for message length (64 bits)
        while ((padded_len % 64) != 56) {
            padded_len++;
        }

        // Allocate space for the padded message
        uint8_t* padded_message = new uint8_t[padded_len + 8];  // +8 for message length in bits
        memcpy(padded_message, message, len);

        // Append the padding byte 0x80 and zeroes
        padded_message[len] = 0x80;
        memset(padded_message + len + 1, 0, padded_len - len - 1);

        // Append the message length in bits at the end
        uint64_t bit_len = len * 8;
        for (int i = 0; i < 8; i++) {
            padded_message[padded_len + i] = (bit_len >> (56 - i * 8)) & 0xFF;
        }

        return padded_len + 8;  // Return total length of padded message
    }

    // Converts 32-bit hash values to a byte array
    static void toByteArray(const uint32_t* hash_values, uint8_t* hash, size_t hash_size) {
        for (size_t i = 0; i < hash_size / 4; i++) {
            hash[i * 4 + 0] = (hash_values[i] >> 24) & 0xFF;
            hash[i * 4 + 1] = (hash_values[i] >> 16) & 0xFF;
            hash[i * 4 + 2] = (hash_values[i] >> 8) & 0xFF;
            hash[i * 4 + 3] = (hash_values[i] >> 0) & 0xFF;
        }
    }
};

#endif
