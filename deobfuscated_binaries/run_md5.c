#include <errno.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

extern unsigned __int128 SECRET(uint64_t a);

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
  unsigned __int128 x = SECRET(n);
  printf("%016"PRIx64"%016"PRIx64"\n",(uint64_t)(x>>64),(uint64_t)x);
  return 0;
}
