#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "HashFunction.h"

int main() {
    // Input message from the user
    char message[256];
    printf("Enter a message to hash: ");
    fgets(message, sizeof(message), stdin);

    // Remove the newline character
    size_t len = strlen(message);
    if (message[len - 1] == '\n') {
        message[len - 1] = '\0';
        len--;
    }

    // Initialize the hash function
    HashFunction hasher;
    hasher.hashMessage((uint8_t*)message, len);

    // Print the resulting hash
    printf("Hash result: ");
    hasher.printHash();

    return 0;
}
