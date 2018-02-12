// Fowler-Noll-Vo Hash (FNV1a)

#include <assert.h>
#include <limits.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// default values recommended by http://isthe.com/chongo/tech/comp/fnv/
const uint32_t Prime = 0x01000193; //   16777619
const uint32_t Seed  = 0x811C9DC5; // 2166136261

// hash a single byte
uint32_t fnv1a_byte(unsigned char oneByte, uint32_t hash) {
  return (oneByte ^ hash) * Prime;
}

/// hash a 32 bit integer (four bytes)
uint32_t fnv1a_dword(uint32_t fourBytes, uint32_t hash) {
  const unsigned char* ptr = (const unsigned char*) &fourBytes;
  hash = fnv1a_byte(*ptr++, hash);
  hash = fnv1a_byte(*ptr++, hash);
  hash = fnv1a_byte(*ptr++, hash);
  return fnv1a_byte(*ptr  , hash);
}

uint32_t SECRET(unsigned long input) {
  return fnv1a_dword((uint32_t)input, Seed);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Call this program with 1 arguments\n");
        return 1;
    }

    unsigned long input = strtoul(argv[1], 0, 10);
    unsigned long output = SECRET(input);

    printf("%lu\n", output);

    return 0;
}
