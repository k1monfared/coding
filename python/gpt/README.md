# About
This is a wrapper for ChatGPT for python that works in terminal. The added benefit here is that you can create features as you wish, for example, here I save all the coversations in log files. I'm saving all the logs in `~/drafts/chatgpt_logs` folder. You can change it to somewhere else, it is in the `log_conversation()` function in `logged_chat.py` file.

# Steps

1. Clone and install the [`langchain`](https://langchain.readthedocs.io/en/latest/index.html) packege.  
    - Unfortunately, it is not on conda or conda-forge, but it is on pypi and you can install it by:

    ```
    pip install langchain
    ```

2. Create an env variable called `OPENAI_API_KEY` with its value being your api key.
    - One way to do this permanently is by adding a line like this to `~/.bashrc`:

    ```
    export OPENAI_API_KEY="your_api_key"
    ```

3. create an alias for the python script in your `~/.bashrc`.
    - I use conda for virtual environment and package management and I've installed the package in an env called `gpt`. So I'll have to activate that env first and then call the script.  

    ```
    alias gpt="conda activate gpt && python path_to_gpt_script/logged_chat.py"
    ```
    - Another way would be to directly call the python from the address of that env.
    ```
    alias gpt="$HOME/anaconda3/envs/gpt/bin/python path_to_gpt_script/logged_chat.py"
    ```

4. Source the bashrc:
    ```
    source ~/.bashrc
    ```
5. Start conversation:
    ```
    gpt
    ```
