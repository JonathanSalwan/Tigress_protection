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

/* fac represents some random computation that
   separates iterations of fib.*/
void fac (int n) {
  int p=1;
  int i;
  for (i=1; i<=n; i++) {
        p*=i;
  }
  printf("fac(%i)=%i\n",n,p);
}

/* fib will be interpreted, and is reentrant: call it
   multiple times until operation>0. At this time the
   computation has terminated. */
void fib(int* operation, int n, int* result) {
  int a=0;
  int b=1;
  int s=1;

  int i;
  for (i=1; i<n; i++) {
    s=a+b;
    a=b;
    b=s;
    /* printf("FIB=%i\n",s); */
  }
  *result=s;
}

int main (int argc, char** argv) {
   int operation;                  
   int result;
   int bogus1;
   int bogus2;

   /********************************************************************************/
  /* first test */
   printf("FIRST TEST\n");
   operation = -10;                      /* operation<0 means to start a new fib computation */              
   srand(123456);
   int n=rand() % 20 + 1;
   fib(&operation,n,&result);            /* initialize fib, function arguments are saved, and execute 10 instructions */

   while (operation < 0) {               /* returning operation<0 means we're not done */
      fac(10);                           /* intersperse other computations */
      operation = 10;
      fib(&operation,bogus1,&bogus2);    /* resume fib, and execute 10 instructions */
      /* printf("operation=%i\n",operation); */
   } 
   printf("fib(%i)=%i\n",n,result);     /* We've reached here because operation>0, i.e. we're done! */

   /********************************************************************************/
   /* second test */
   printf("\nSECOND TEST\n");
   operation = -10;                        /* initialize fib and execute 10 instructions */
   n = 5;
   fib(&operation,n,&result);
   operation = 10;
   fib(&operation,bogus1,&bogus2);         /* resume fib, and execute 10 instructions */
   if (operation < 0) {                    /* are we done? */
        fac(10);                           /* intersperse other computations */
        operation = 1000;
        fib(&operation,bogus1,&bogus2);    /* resume fib, and make sure we finish executing */
   }
   printf("fib(%i)=%i\n",n,result);        /* start fib again, execute 1000 instructions */

   operation = 1000;
   fib(&operation,bogus1,&bogus2)  ;       /* resume fib, even if we're done executing */
   printf("fib(%i)=%i\n",n,result);        /* we should get the same result            */

   /********************************************************************************/
   /* third test */
   printf("\nTHIRD TEST\n");
   operation = -10000;                   
   n = 20;
   fib(&operation,n,&result);
   printf("fib(%i)=%i\n",n,result);        /* start fib again, execute 1000 instructions */

  return 0;
}
