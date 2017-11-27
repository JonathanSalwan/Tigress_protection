#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <errno.h>

extern uint64_t SECRET(uint64_t a);

int main(int argc, char** argv)
{
  if (argc < 2) {
    fprintf(stderr, "Usage: %s n\n", argv[0]);
    return 1;
  }
  uint64_t n = strtoull(argv[1], NULL, 0);
  if (errno != 0) {
    perror("unable to represent the input as an uint64");
    return 1;
  }
  printf("%lu\n", SECRET(n));
  return 0;
}
