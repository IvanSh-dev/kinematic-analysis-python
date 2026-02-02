Kinematic Analysis Tool: Slider-Crank Mechanism ⚙️

A desktop application built with Python and Tkinter for calculating and visualizing the velocity vector diagrams (velocity plans) of a slider-crank mechanism.
🎯 Overview

This tool automates the process of kinematic analysis, which is traditionally done manually in mechanical engineering. By inputting the geometric and motion parameters, the software instantly generates a precise velocity vector plan.
🚀 Key Features

    • Interactive GUI: User-friendly interface built with Tkinter for real-time data entry.

    • Vector Visualization: Dynamic rendering of velocity vectors for Point A, Point B, and the Connecting Rod (AB).

    • Mathematical Accuracy: Implements trigonometric models to calculate angular velocities and linear motion components.

    • Legend System: Color-coded vectors for better readability (Red for Va​, Blue for Vb​, Green for Vab​).

🛠 Tech Stack

    • Python 3.x

    • Tkinter: For the graphical user interface and canvas drawing.

    • Math Module: For precise trigonometric and algebraic computations.

📈 Mathematical Logic Included

The program processes the following parameters:

    Crank Length and Rod Length.

    Crank Angle (converted to radians for calculation).

    Angular Velocity of the crank.

It calculates the X and Y components of velocities, taking into account the geometry of the mechanism to find the relative velocity of the connecting rod and the sliding speed of the piston.
🖥️ How to Use

    Clone the repository:
    Bash

    git clone https://github.com/IvanSh-dev/kinematic-analysis-python.git

    Run the application:
    Bash

    python main.py

    Enter the dimensions, angle, and velocity, then click "Побудувати план швидкостей".
