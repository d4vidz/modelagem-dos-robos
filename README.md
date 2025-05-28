# 2R Planar Robot Simulation

This project simulates a simple 2R (two-revolute-joint) planar robot using Python and the Robotics Toolbox for Python.

## Requirements
- Python 3.8+
- [Robotics Toolbox for Python](https://github.com/petercorke/robotics-toolbox-python)
- numpy
- spatialmath

All required packages are listed in `requirements.txt`.

## Setup Instructions

1. **Create and activate a virtual environment (recommended):**

   On Windows (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the simulation:**
   ```powershell
   python 2R_rotacionais.py
   ```

This will print the robot details, compute the forward kinematics for a sample configuration, and open an interactive window to visualize the robot.

---

If you encounter issues with the visualization, ensure you have all required packages installed and that your Python environment is activated.
