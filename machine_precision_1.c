#include <stdio.h>
#include <float.h>
#include <math.h>

int main() {
    // Machine precision (epsilon) for the C float data type
    float machine_precision = FLT_EPSILON;

    // Storing π in a float variable
    float pi_stored = (float)M_PI;

    // True value of π
    double pi_true = M_PI;

    // Relative error in storing π
    float relative_error = fabs((pi_stored - pi_true) / pi_true);

    // Display the results
    printf("Machine Precision (float): %e\n", machine_precision);
    printf("Storing π in float: %.10f\n", pi_stored);
    printf("Relative Error in Storing π: %e\n", relative_error);

    return 0;
}
