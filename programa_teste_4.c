#include <stdio.h>
#include <stdlib.h>

/*

  *** Autor: Hilário Tomaz
  -- Data: 25/04/2019

*/

int main()
{

    printf(fatorial(5)); // Chamada Função Fatorial

    return 1;
}

int fatorial(int n)
{
    int res;

    if (n < 1)
        res = 1;
    else
        res = n * fatorial(n - 1);

    return res;
}
