#include <stdio.h>
#include <stdin.h>

int main() {

    int x = 0, y;

    if( x >= 10 )
        x = x + 1;

    if( x == 20.0 ) {
        float y = 2.0;
        x = x / y;
    } else {
        x = 2 * x + 1 / 2 - 5;
    }

    return 0;

}

int soma(int x, char y) {

    int s = x + y;

    char a;

    a = 'O';

    return s;

}


