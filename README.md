# Specific Heat Approximation By Interpolation

This script is written in Python and utilizes interpolation methods, such as Spline Interpolation, Lagrange Interpolation, and Neville's Algorithm, to calculate Specific Heat of temperature nodes of a substance, and compares the approximations to measured data.

# SAMPLE OUTPUT:


For x = 25 degrees CELSIUS, the actual Specific Heat is 4180 J/(C kg).
        We will use dataset 1:
        Our given (water temperatures) to be used are: [20, 40, 50, 80, 90]
        The Specific heats evaluated at the nodes are: [4182, 4179, 4182, 4198, 4208]
        Now, f(x) is approximated with several interpolation methods: 
        


Use Cubic Spline Interpolation with data set 1:

S_0(x) = -6.01656*(0.05*x - 1.0) + 0.000377*(x - 20)**3 + 4182 for [20,40]
S_1(x) = 6.06624*(0.025*x - 1.0) - 0.000779*(x - 40)**3 + 0.022624*(x - 40)**2 + 4179 for [40,50]
S_2(x) = 18.52225*(0.02*x - 1.0) + 0.000206*(x - 50)**3 - 0.000745*(x - 50)**2 + 4182 for [50,80]
S_3(x) = 70.5176*(0.0125*x - 1.0) - 0.000593*(x - 80)**3 + 0.01778*(x - 80)**2 + 4198 for [80,90]

Spline in our range, for Final Approximation:  -6.01656*(0.05*x - 1.0) + 0.000377*(x - 20)**3 + 4182 

FINAL APPROXIMATION: 4180.542985

Relative error for Spline:  0.00012990071770335986


Use Lagrange Interpolation with data set 1:

Lagrange Polynomial is:  697*(x - 90)*(x - 80)*(x - 50)*(x - 40)/420000 - 4179*(x - 90)*(x - 80)*(x - 50)*(x - 20)/400000 + 697*(x - 90)*(x - 80)*(x - 40)*(x - 20)/60000 - 2099*(x - 90)*(x - 50)*(x - 40)*(x - 20)/360000 + 263*(x - 80)*(x - 50)*(x - 40)*(x - 20)/87500 

FINAL APPROXIMATION: 4179.4415922619055

Relative error for Lagrange:  0.00013359036796519182


Use Nevilles method with data set 1:


Q_( 4 , 4 ) = 4179.4415922619055
[[4182.            0.            0.            0.            0.        ]
 [4179.         4181.25          0.            0.            0.        ]
 [4182.         4174.5        4180.125         0.            0.        ]
 [4198.         4168.66666667 4176.6875     4179.83854167    0.        ]
 [4208.         4143.         4184.70833333 4174.28125    4179.44159226]]

FINAL APPROXIMATION:  4179.4415922619055

Relative error for Nevilles Method:  0.00013359036796519182

--------------------------------------------------------------
 
For x = 85 degrees CELSIUS, the actual Specific Heat is 4203 J/(C kg).
        We will use dataset 2:
        Our given (water temperatures) to be used are: [10, 30, 50, 70, 90]
        The Specific heats evaluated at the nodes are: [4192, 4178, 4182, 4191, 4208]
        Now, f(x) is approximated with several interpolation methods: 
        


Use Cubic Spline Interpolation with data set 2:

S_0(x) = -9.30357*(0.1*x - 1.0) + 0.000576*(x - 10)**3 + 4192 for [10,30]
S_1(x) = -7.17858*(0.0333333333333333*x - 1.0) - 0.000629*(x - 30)**3 + 0.034554*(x - 30)**2 + 4178 for [30,50]
S_2(x) = 19.375*(0.02*x - 1.0) + 0.000317*(x - 50)**3 - 0.003214*(x - 50)**2 + 4182 for [50,70]
S_3(x) = 44.75002*(0.0142857142857143*x - 1.0) - 0.000263*(x - 70)**3 + 0.015804*(x - 70)**2 + 4191 for [70,90]

Spline in our range, for Final Approximation:  44.75002*(0.0142857142857143*x - 1.0) - 0.000263*(x - 70)**3 + 0.015804*(x - 70)**2 + 4191 

FINAL APPROXIMATION: 4203.257565

Relative error for Spline:  6.128122769447678e-05


Use Lagrange Interpolation with data set 2:

Lagrange Polynomial is:  131*(x - 90)*(x - 70)*(x - 50)*(x - 30)/120000 - 2089*(x - 90)*(x - 70)*(x - 50)*(x - 10)/480000 + 2091*(x - 90)*(x - 70)*(x - 30)*(x - 10)/320000 - 1397*(x - 90)*(x - 50)*(x - 30)*(x - 10)/320000 + 263*(x - 70)*(x - 50)*(x - 30)*(x - 10)/240000 

FINAL APPROXIMATION: 4202.234375

Relative error for Lagrange:  0.00018216155127290031


Use Nevilles method with data set 2:


Q_( 4 , 4 ) = 4202.234375
[[4192.           0.           0.           0.           0.       ]
 [4178.        4139.5          0.           0.           0.       ]
 [4182.        4189.        4232.3125       0.           0.       ]
 [4191.        4197.75      4201.03125   4193.2109375    0.       ]
 [4208.        4203.75      4203.        4202.8359375 4202.234375 ]]

FINAL APPROXIMATION:  4202.234375

Relative error for Nevilles Method:  0.00018216155127290031

--------------------------------------------------------------
