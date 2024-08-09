sudo apt-get install graphviz

conda create -n mgraph python=3.12 pip
conda activate mgraph

pip install -r requirements.txt

To run the app:
uvicorn app.main:app --reload