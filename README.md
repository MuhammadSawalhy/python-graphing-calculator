# Python Graphing Calculator

Graphing calculator built with Pyside2 (Qt) and Matplotlib to create the plot. The app is tested and CSS stylesheet is used to give it a more pleasant and appealing look.

## Run the app

Make sure to install all requirements: `pip install -r requirements.txt`.

```bash
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

**After installing all requirements:**

```bash
python main.py
# or just run
make
```

## Test the app

```bash
PYTHONPATH="$PYTHONPATH:$(pwd)" pytest
# or just run
make tests
```

## Demo of the app

https://github.com/MuhammadSawalhy/python-graphing-calculator/assets/42011920/fda20305-db6e-4bcb-ac06-66b2c9834a8c

