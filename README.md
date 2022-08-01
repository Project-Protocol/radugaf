## How to run the project in its current development stage

**NOTE:** Make sure you have at least [python3.8](https://www.python.org/downloads/macos/) installed on your system. 

Create a virtual environment (so that any installed package would not cause issues across the system)
```python
python3 -m venv env
```

Once python is installed and you have created the virtual environment, activate it
```python
source env/bin/activate
```

Then simply install the required packages (currently we're only using: [domonic](https://pypi.org/project/domonic/)  and [dataclass wizard](https://pypi.org/project/dataclass-wizard/))
```python
pip install domonic dataclass-wizard
```

Then you should mostly be ready to go :)

