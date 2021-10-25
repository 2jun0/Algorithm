#include <stdio.h>

int main(void) {
  char t;
  char c;
  char l = 0;
  while (scanf("%c", &c) != -1){
    if (t == c) l++;
    else {
      if (l > 2) printf("%c%d", t,l);
      else if (l == 1) printf("%c", t);
      else if (l == 2) printf("%c%c", t,t);
      l = 1;
      t = c;
    }
  }

  if (l > 2) printf("%c%d", t,l);
  else printf("%c", t);
}