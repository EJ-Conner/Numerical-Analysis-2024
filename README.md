# Numerical Analysis 2024 

Here are all the numerical methods I have created in 2024. This is a toolkit for exploring and applying fundamental numerical techniques. Whether you're a student, researcher, or developer, you'll find practical implementations and insightful visualizations here.

## What's Inside?

This toolkit is organized into key numerical analysis categories:

* **🔍 Root Finding Algorithms:**
    * **Bisection Method:** (`Bisection_Method.py`) A reliable bracketing method for finding roots.
    * **Newton's Method:**
        * (`Newtons_Method_Root_Solver.py`) Classic Newton for roots.
        * (`Newtons_Method_2x2.py`) Extends Newton's method to solve 2x2 systems.
        * (`Newtons_Method_Central_Diff.py`) Uses central difference approximation for derivatives.
* **📊 Linear Algebra & Systems:**
    * **Gaussian Elimination:**
        * (`Gaussian_Elim_3x3.py`) Solves 3x3 linear systems.
        * (`Gaussian_Pivot_Solver.py`) Implements Gaussian elimination with pivoting for stability.
* **📉 Curve Fitting & Regression:**
    * **Curve Fitting:** (`Curve_Fitting_Divided_Difference.py`) Uses divided differences for polynomial interpolation.
    * **Linear Regression:** (`Linear_Regression.py`) Performs linear regression analysis.
* **🌌 N-Body Simulations:**
    * **Leap Frog 3 Body 3D:** (`Leap_Frog_3_body_3D.py`) Simulates the 3D motion of three bodies using the Leap Frog method.
* **📈 Ordinary Differential Equations (ODEs):**
    * **Runge-Kutta Methods:**
        * (`RK2_vs_T2.py`) Compares RK2 with Taylor series solutions.
        * (`RK4_RK8.py`) Implements RK4 and RK8 methods for high-accuracy solutions.
    * **Taylor Series Methods:**
        * (`Taylor_Series_Approx_of_sin.py`) Approximates sine function using Taylor series.
        * (`Taylors_Method_Over_DFs.py`) Demonstrates Taylor's method for solving ODEs.
        * (`Taylors_Method_Two_ODE.py`) Solves systems of two ODEs using Taylor's method.
* **🌀 Phase Plane Analysis:**
    * (`Phase_Plane_ODE_Solver.py`) Generates phase plane plots for ODE systems.
    * (`Phase_Planes_Visualization.py`) Visualizes phase planes for various systems.
* **🎨 Simple Plotting Utilities:**
    * (`Function_Derivative_Plot.py`) Plots a function and its derivative.
    * (`User_Function_Plotter.py`) Creates plots of user-defined functions.
 

## Getting Started

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/EJ-Conner/Numerical-Analysis-2024.git](https://github.com/EJ-Conner/Numerical-Analysis-2024.git)
    cd Numerical-Analysis-Tools
    ```
2.  **Install Dependencies (if any):**
    ```bash
    pip install math sys numpy sympy matplotlib scipy IPython mpl_toolkits 
    ```
3.  **Run a Script:**
    ```bash
    python <numerical script name here>
    ```
