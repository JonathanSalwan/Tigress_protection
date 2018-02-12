#ifdef __APPLE__
#include<Availability.h>
#undef __OSX_AVAILABLE_STARTING
#define __OSX_AVAILABLE_STARTING(_mac, _iphone)
#undef __OSX_AVAILABLE_BUT_DEPRECATED
#define __OSX_AVAILABLE_BUT_DEPRECATED(_osxIntro, _osxDep, _iosIntro, _iosDep)
#undef __OSX_AVAILABLE_BUT_DEPRECATED_MSG
#define __OSX_AVAILABLE_BUT_DEPRECATED_MSG(_osxIntro, _osxDep, _iosIntro, _iosDep, _msg)
#undef __BLOCKS__
#endif

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fac(int n) {
  int s=1;
  int i;
  for (i=2; i<=n; i++) {
    s *= i;
  }
  printf("fac(%i)=%i\n",n,s);
}

void fib(int n) {
  int a=0;
  int b=1;
  int s=1;

  int i;
  for (i=1; i<n; i++) {
    s=a+b;
    a=b;
    b=s;
  }
  printf("fib(%i)=%i\n",n,s);
}

int main (int argc, char** argv) {
  fac(1);
  fib(1);
  fac(5);
  fib(5);
  fac(10);
  fib(10);
  return 0;
}
