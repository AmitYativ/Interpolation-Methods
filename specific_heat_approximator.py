#!/usr/bin/env python

# Author: Amit Yativ

import numpy as np
from sympy import Symbol, factor, lambdify

""" Program Description:
This program utilizes methods of approximation, via interpolation,
to approximate the Specific Heat, with units of
joules per Celsius and kilogram, i.e. J/(C kg), of water at a certain
temperature in degrees Celsius, given measured data. Other substances
can be applied to this instead.

"""

def main():

    # Given data set 1
    (list_x1, list_fx1) = ([20, 40, 50, 80, 90],[4182, 4179, 4182, 4198, 4208])

    # Given data set 2
    (list_x2, list_fx2) = ([10, 30, 50, 70, 90], [4192, 4178, 4182, 4191, 4208])

    # Temperatures to approximate Specific Heat of, and their
    # measured specific heats for comparison
    (x1, fx1) = (25, 4180)
    (x2, fx2) = (85, 4203)

    # List of data sets in tuples
    data_sets = [(list_x1, list_fx1), (list_x2,list_fx2)]

    # List of nodes to be approximated, and their measured values for comparison.
    target_nodes = [(x1,fx1),(x2,fx2)]

    for i in range(len(data_sets)):
        set_num = i + 1
        print(""" \nFor x = {} degrees CELSIUS, the actual Specific Heat is {} J/(C kg).
        We will use dataset {}:
        Our given (water temperatures) to be used are: {}
        The Specific heats evaluated at the nodes are: {}
        Now, f(x) is approximated with several interpolation methods: 
        """.format(target_nodes[i][0],target_nodes[i][1],set_num,data_sets[i][0], data_sets[i][1]))

        # ---------------------- (1) Spline Interpolation ----------------------

        print('\n\nUse Cubic Spline Interpolation with data set {}:\n'.format(set_num))

        # Build Spline, Get Spline polynomial within target node interval
        spline = splineConstructor(data_sets[i][0], data_sets[i][1], target_nodes[i][0])

        # Evaluate Spline polynomial at node, find error
        spline_approx = spline(target_nodes[i][0])
        spline_error = relativeError(target_nodes[i][1], spline_approx)
        print('FINAL APPROXIMATION:', spline_approx)
        print('Relative error for Spline: ', spline_error)

        # ---------------------- (2) Lagrange Interpolation ----------------------

        print('\n\nUse Lagrange Interpolation with data set {}:\n'.format(set_num))

        # Build Lagrange Polynomial
        lagrange_poly = lagrangePolynomial(data_sets[i][0], data_sets[i][1])

        # Evaluate Lagrange Polynomial, find error
        lagrange_approx = lagrange_poly(target_nodes[i][0])
        lagrange_error = relativeError(target_nodes[i][1], lagrange_approx)

        print('FINAL APPROXIMATION:', lagrange_approx)
        print('Relative error for Lagrange: ', lagrange_error)

        # ---------------------- (3) Neville's Algorithm ----------------------

        print('\n\nUse Nevilles method with data set {}:\n\n'.format(set_num))

        # Build Table
        neville_approx, neville_table = nevillesMethod(target_nodes[i][0], data_sets[i][0], data_sets[i][1])

        # Print Table, find error
        print(neville_table)
        neville_error = relativeError(target_nodes[i][1], neville_approx)

        #  We Consider the bottom-right table entry - The highest degree approximation.
        print('\nFINAL APPROXIMATION: ', neville_approx)
        print('Relative error for Nevilles Method: ', neville_error)
        print('\n--------------------------------------------------------------')

# --------------------------------- ALGORITHMS ---------------------------------

#  Relative Error Function
def relativeError(actual, approx):
    rel_error = abs(actual - approx) / abs(actual)
    return rel_error


# Vector for initial values in lists
def vec(m): z = [0] * m; return (z)


# Spline Interpolation Algorithm
def splineConstructor(list_x, list_fx, evaluatee):
    n = len(list_x)
    h = vec(n - 1);
    alpha = vec(n - 1);
    l = vec(n + 1)
    u = vec(n);
    z = vec(n + 1) \
    ; b = vec(n)
    c = vec( n +1) ; d = vec(n)
    for i in range(0, n - 1):
        h[i] = list_x[ i +1] - list_x[i]
    for i in range(1, n - 1):
        alpha[i] = (3./h[i] ) *(list_fx[ i +1] - list_fx[i] ) -(3./h[i - 1] ) *(list_fx[i] - list_fx[ i -1])
        l[0] = 1 ; u[0] = 0 ; z[0] = 0
    for i in range(1, n - 1):
        l[i] = 2* (list_x[i + 1] - list_x[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
        l[len(l) - 1] = 1;
        z[len(z) - 1] = 0;
        c[len(c) - 1] = 0
    for j in reversed(range(n - 1)):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (list_fx[j + 1] - list_fx[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3.
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    x = Symbol('x')
    for j in range(0, n - 1):
        s_jx = round(list_fx[j], 6) + factor((round(b[j], 6) * (x - list_x[j]))) + round(c[j], 6) * (
                    x - list_x[j]) ** 2 + round(d[j], 6) * (x - list_x[j]) ** 3
        print('S_{}(x) = {} for [{},{}]'.format(j,s_jx,list_x[j],list_x[j + 1]))
        if evaluatee >= list_x[j] and evaluatee <= list_x[j + 1]:
            spline_to_use = str(s_jx)
    print('\nSpline in our range, for Final Approximation: ', spline_to_use,'\n')
    spline_to_use = lambdify(x,spline_to_use)
    return spline_to_use


# Neville's Method
def nevillesMethod(x, list_x, list_fx, Q_table=None):
    n = np.size(list_x) - 1;
    if (Q_table == None):
        Q_table = np.zeros((n + 1, n + 1));

    for i in range(0, n + 1):
        Q_table[i][0] = list_fx[i];

    for i in range(1, n + 1):
        for j in np.arange(1, i + 1):
            Q_table[i][j] = 0.0
            Q_table[i][j] += (((x - list_x[i - j]) * Q_table[i][j - 1] - (x - list_x[i]) * (Q_table[i - 1][j - 1])) / (
                        list_x[i] - list_x[i - j]))

    print('Q_(', i, ',', j, ') =', Q_table[i][j])

    return Q_table[n][n], Q_table;


# Lagrange Interpolation Method
def lagrangePolynomial(nodes, function_nodes):
    degree_specification = len(nodes) - 1
    x = Symbol("x")
    whole_polynomial = 0
    nodes = nodes[:degree_specification + 1]
    for coefficients in range(0, len(nodes)):
        current_node = nodes[coefficients]
        rest_of_nodes = nodes[:coefficients] + nodes[coefficients + 1:]
        coeffcient_polynomial_numerator = 1
        coeffcient_polynomial_denominator = 1
        for remaining_nodes in rest_of_nodes:
            coeffcient_polynomial_numerator = coeffcient_polynomial_numerator \
                                              * (x - remaining_nodes)
        for remaining_nodes2 in rest_of_nodes:
            coeffcient_polynomial_denominator = coeffcient_polynomial_denominator \
                                                * (current_node - remaining_nodes2)
        coeffient_polynomial = function_nodes[coefficients] \
                               * (coeffcient_polynomial_numerator \
                                  / coeffcient_polynomial_denominator)
        whole_polynomial += coeffient_polynomial
    print('Lagrange Polynomial is: ', whole_polynomial)
    whole_polynomial = lambdify(x,whole_polynomial)
    return whole_polynomial


if __name__ == '__main__':
    main()
