# specimen-custody-chain 


## Setup .venv
Setup your virutalenv venv with something like this... 

```sh
brew install python@3.12 ## to get python, if you do'nt already have it! 
/opt/homebrew/Cellar/python\@3.10/3.10.13_2/bin/python3.10 -m venv .venv
source ./.venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```


## Run the application
```sh
source ./.venv/bin/activate
streamlit run ./src/app.py
```

## Set Classpath
Your classpath must be set to this directory, plus ./src, like:

`export PYTHONPATH=$PYTHONPATH:[this project directory]/src`

