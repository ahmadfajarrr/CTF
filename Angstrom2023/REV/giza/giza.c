
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define N 428


void cofac(int mat[N][N], int t[N][N],
                 int p, int q, int n) {
    int a = 0, b = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != p && j != q)
            {
                t[a][b++] = mat[i][j];
 
                if (b == n - 1)
                {
                    b = 0;
                    a++;
                }
            }
        }
    }
}
 
int det(int mat[N][N], int n)
{
    int D = 0;
 
    if (n == 1)
        return mat[0][0];
 
    int temp[N][N];
 
    int sign = 1;
 
    for (int f = 0; f < n; f++) {

        cofac(mat, temp, 0, f, n);
        D += sign * mat[0][f]* det(temp, n - 1);
        sign = -sign;
    }
 
    return D;
}

void main() {
    int flag[N];

    flag[0] = (int)getchar();

    for (int i = 1; i < N; i++) {
        int ch = (int)getchar();
        flag[i] = flag[i - 1] + ch;
    }

    for (int i = 0; i < N; i++) {
        int mi[N][N];
        for (int r=0; r < N; r++) {
            for (int s=0; s < N; s++) {
                if (r == s) {
                    mi[r][s] = m[r][s] - flag[i];
                } else {
                    mi[r][s] = m[r][s];
                }
            }
        }

        int i = det(mi, N);
        if (i != 0) {
            printf("Buried in the sands...");
            exit(1);
        }
    }

    printf("You made it to the top!");
}
