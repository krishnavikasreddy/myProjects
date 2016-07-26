#include<stdio.h>

int main(char *argv,char *argc){
  int i[3][3];
  int **p=i;

  i[0][0]=1;
  i[0][1]=10;
  i[0][2]=11;
  i[1][0]=12;

  printf("\n%p",p);
  printf("\n%d",*(p+2));
  
  return 0;
}
