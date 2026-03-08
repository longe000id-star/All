←
#include <stdio.h>

typedef struct {
    int a[6];
    double d;
} struct_t;

double fun(int i) {
    volatile struct_t s;
    s.d = 3.14;
    s.a[i] = 1073741824; /* Possibly out of bounds */
    return s.d;
}

int main() {
    int input;
    // 用户输入
    while (1) {
        printf("请输入一个整数 (例如 0, 1, 2 或者 -1 退出): ");
        scanf("%d", &input);
        
        if (input == -1) {
            break;  // 如果输入 -1，就退出循环
        }

        printf("fun(%d) => %f\n", input, fun(input));  // 调用 fun 函数并输出结果
    }

    return 0;
}
