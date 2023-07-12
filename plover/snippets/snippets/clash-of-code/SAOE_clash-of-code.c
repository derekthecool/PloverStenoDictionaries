#include <stdio.h>
#include <stdlib.h>
#include <string.h>
main() {
char *p,*l=0;
// Read all stdin
getdelim(&p,&l,0xff,stdin);
// Or read just a line
// getline(&p,&l,stdin);
printf("%s\n", p);
}
