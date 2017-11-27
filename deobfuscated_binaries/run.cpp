#include <cstdlib>
#include <cstdint>
#include <iostream>
#include <sstream>

extern "C" uint64_t SECRET(uint64_t a);

int main(int argc, char** argv)
{
  if (argc < 2) {
    std::cerr << "Usage: " << argv[0] << " n" << std::endl;
    return 1;
  }
  uint64_t n;
  std::istringstream ss(argv[1]);
  ss >> n;
  std::cout << SECRET(n) << std::endl;
  return 0;
}
