←
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void copyij(int** src, int** dst) {
    int i, j;
    for (i = 0; i < 20480; i++) {
        for (j = 0; j < 20480; j++) {
            dst[i][j] = src[i][j];
        }
    }
}

void copyji(int** src, int** dst) {
    int i, j;
    for (j = 0; j < 20480; j++) {
        for (i = 0; i < 20480; i++) {
            dst[i][j] = src[i][j];
        }
    }
}

int main() {
    int **src, **dst;
    clock_t start, end;
    int i, j;

    // 动态分配内存
    src = (int**)malloc(20480 * sizeof(int*));
    dst = (int**)malloc(20480 * sizeof(int*));
    for (i = 0; i < 20480; i++) {
        src[i] = (int*)malloc(20480 * sizeof(int));
        dst[i] = (int*)malloc(20480 * sizeof(int));
    }

    // 初始化矩阵
    for (i = 0; i < 20480; i++) {
        for (j = 0; j < 20480; j++) {
            src[i][j] = i * j;
        }
    }

    // 测量 copyij 执行时间
    start = clock();
    copyij(src, dst);  // 执行复制操作
    end = clock();
    printf("Time taken for copyij (20480x20480): %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    // 测量 copyji 执行时间
    start = clock();
    copyji(src, dst);  // 执行复制操作
    end = clock();
    printf("Time taken for copyji (20480x20480): %lf seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    // 释放内存
    for (i = 0; i < 20480; i++) {
        free(src[i]);
        free(dst[i]);
    }
    free(src);
    free(dst);

    return 0;
}
