#include <stdio.h>

int main() {
    float number;
    printf("Enter a floating-point number: ");
    scanf("%f", &number);  // Read a float input from the user
    printf("You entered: %.2f\n", number);
    return 0;
}
