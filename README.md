# 2R Planar Robot Simulation

This project simulates a simple 2R (two-revolute-joint) planar robot using Python and the Robotics Toolbox for Python.

## Requirements
- Python 3.9+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- [Robotics Toolbox for Python](https://github.com/petercorke/robotics-toolbox-python)

All dependencies are listed in `requirements.txt`.

## Setup Instructions

1. **Install uv (if not already installed):**

   On Windows (PowerShell):

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   On macOS/Linux:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone or download this project** to your local machine

3. **Install dependencies using uv:**

   ```powershell
   uv pip install -r requirements.txt
   ```

   This will:
   - Create a virtual environment in `.venv/` (if not present)
   - Install all required packages

## Running the Program

1. **Run the simulation:**

   ```powershell
   uv run python 2R_rotacionais.py
   ```

   Or manually activate the environment and run:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   python 2R_rotacionais.py
   ```

This will print the robot details, compute the forward kinematics for a sample configuration, and open an interactive window to visualize the robot.

## For Project Contributors

- To add new dependencies, update `requirements.txt` and reinstall with `uv pip install -r requirements.txt`.
- You do not need a `pyproject.toml` for this script-based workflow.

---

**Note:** If you encounter issues with the visualization, ensure you have all required packages installed and that your Python environment is activated.
