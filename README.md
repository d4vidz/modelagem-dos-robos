# 2R Planar Robot Simulation

This project simulates a simple 2R (two-revolute-joint) planar robot using Python and the Robotics Toolbox for Python.

## Requirements
- Python 3.9+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager
- [Robotics Toolbox for Python](https://github.com/petercorke/robotics-toolbox-python)

All dependencies are managed via `uv` and locked in `uv.lock` for reproducible builds.

## Setup Instructions

### For New Users (Setting up the exact same environment)

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

3. **Install the exact same dependencies using uv:**
   ```powershell
   cd "path\to\project"
   uv sync
   ```

   This will:
   - Create a virtual environment in `.venv/`
   - Install the exact same package versions from `uv.lock`
   - Ensure 100% reproducible dependency resolution

### Alternative: Manual virtual environment setup

If you prefer not to use `uv`, you can still use the traditional approach:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running the Program

1. **Activate the environment and run the simulation:**

   With uv:

   ```powershell
   uv run python 2R_rotacionais.py
   ```

   Or manually activate the environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   python 2R_rotacionais.py
   ```

This will print the robot details, compute the forward kinematics for a sample configuration, and open an interactive window to visualize the robot.

## For Project Contributors

### Adding new dependencies:

```powershell
uv add package-name
```

### Updating dependencies:

```powershell
uv lock --upgrade
```

### Generating requirements.txt for compatibility:

```powershell
uv export --format requirements-txt --output-file requirements.txt
```

---

**Note:** The `uv.lock` file ensures that everyone gets the exact same dependency versions, making the environment 100% reproducible across different machines and platforms.

If you encounter issues with the visualization, ensure you have all required packages installed and that your Python environment is activated.
