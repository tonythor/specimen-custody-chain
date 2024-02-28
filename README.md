# llm

A project leveraging LLM's and prompts!


### Setup .venv
Setup your virutalenv venv with something like this... 

```sh
brew install python@3.11 ## to get python, if you do'nt already have it! 

/opt/homebrew/Cellar/python\@3.11/3.11.7_1/bin/python3 -m venv .venv
source ./.venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```



### Run the application
```sh
source ./.venv/bin/activate
streamlit run ./src/app.py
```