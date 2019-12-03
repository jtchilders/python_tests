#include <stdio.h>
#include <stdlib.h>

void print_TEST()
{
   const char* s = getenv("TEST");
   printf("TEST :%s\n",(s!=NULL)? s : "getenv returned NULL");
}



