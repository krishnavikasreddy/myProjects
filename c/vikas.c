#include<stdio.h>

int main(void){
  int i=5;
  char a='a';
  int *i1= &i;
  char *a1 = &a;

  printf("%p\n",a1);
  (a1)++;
  printf("%p\n",a1);
  printf("%d",i);
  return 0;
}
