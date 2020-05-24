#include <stdio.h>

int main()
{
    char arr[10];

    // when we compile with the `-fno-stack-protector` flag
    // if we keep `i` relatively small, we may not get segmentation fault
    // as the system stack is not tried to be overwritten
    for (int i = 0; i < 10000; i++)
        arr[i] = 'a';

    return 0;
}