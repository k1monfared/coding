import os
import json
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import datetime

llm = OpenAI(temperature=0, max_tokens=1000)  # type: ignore
prompt = PromptTemplate(
    input_variables=["prompt"],
    template="""{prompt}""",
)
non_chain = LLMChain(prompt=prompt, llm=llm)

def chat(user_input):
    result = non_chain.run(user_input)
    return result

def log_conversation(filename, speaker, speech):
    log_dir = os.path.join(os.path.expanduser('~'), "drafts/chatgpt_logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    with open(os.path.join(log_dir, filename), 'a') as f:
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("{} {}: {}\n\n---------------\n\n".format(dt, speaker, speech))

def conversation():
    dt = datetime.datetime.now()
    filename = "chatgpt_{}.log".format(dt.strftime("%Y%m%d_%H%M%S"))
    user_input = " "
    while user_input:
            user_input = input("\n--\n You: ")
            if not len(user_input):
                return
            log_conversation(filename, speaker = "You", speech = user_input)
            result = non_chain.run(user_input)
            log_conversation(filename, speaker = "ChatGPT", speech = result)
            print('\n--\nChatGPT: {}'.format(result))


if __name__ == "__main__":
    conversation()
