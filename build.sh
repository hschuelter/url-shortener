echo "BUILD START"

# create a virtual environment
python3.9 -m venv .venv

# activate the virtual environment
source venv/bin/activate

# install all deps in the venv
python3.9 -m install -r requirements.txt

echo "BUILD END"