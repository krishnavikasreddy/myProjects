#include<stdio.h>
#include<stdlib.h>

void print_numbers(int*, size_t);
void insertion_sort(int*, size_t);
void merge_sort(int* ,size_t, size_t, size_t);

int main(char argc, char** argv) {
  int numbers[3]= {10,-2,-3};
  size_t numbers_size = sizeof(numbers)/sizeof(numbers[0]);
  printf("%lu",numbers_size);
  /* insertion_sort(numbers, numbers_size); */
  /* printf("Insertion ----------------------------\n"); */
  /* print_numbers(numbers,numbers_size); */
  printf("\nMerge Sort------------------------------------\n");
  merge_sort(numbers, numbers_size, 0, numbers_size-1);
  print_numbers(numbers,numbers_size);
  return 0;
}

void print_numbers(int *numbers, size_t size) {
    for(size_t i = 0; i < size; i++) {
    printf("%d\t",numbers[i]);
  }
}

void insertion_sort(int *numbers_array, size_t length_array) {
  for(size_t i=1; i<length_array; i++) {
    int key = *(numbers_array+i);
    size_t k = i;
    for(size_t j=i; j > 0; j--) {
      if (key < *(numbers_array+j)) {
        *(numbers_array+k) = *(numbers_array+j-1);
        k=j-1;
      }
    }
    if (k != i) {
      *(numbers_array+k) = key;
    }
  }
}

void merge_sort(int *numbers_array, size_t length_array, size_t start, size_t end) {
  if (start == end) {
    return;
  }
  size_t middle = (start + end)/2;
  merge_sort(numbers_array,length_array,start,middle);
  merge_sort(numbers_array,length_array,middle+1,end);

  // merge
  size_t i = start;
  size_t j = middle+1;
  size_t k = 0;
   int *temp_array = (int *)malloc((end-start+1)*sizeof(int));
  while (i <= middle && j <=  end) {
    if (*(numbers_array + i) <= *(numbers_array + j)) {
        *(temp_array + k) = *(numbers_array + i);
      i++;
    } else {
      *(temp_array + k) = *(numbers_array + j);
      j++;
    }
    k++;
  }
  while (i <= middle) {
    *(temp_array + k) = *(numbers_array + i);
    i++;
    k++;
  }
  while (j <=  end) {
    *(temp_array + k) = *(numbers_array + j);
    j++;
    k++;
  }
  
  for(k=0; k<=(end-start); k++) {
    *(numbers_array + start + k) = *(temp_array + k);
  }
  free(temp_array);
}
