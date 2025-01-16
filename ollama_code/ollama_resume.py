from ollama import chat #ollama->library and chat->function to interact with llm
from ollama import ChatResponse #ChatResponse->class
import ollama

with open('/Users/aparimeyatiwari/Downloads/MSQ_Bot_Podcast/ollama_code/output_resume1.txt','r') as file:
    data = file.read()


response : ChatResponse = chat(model='custom_ner_model',messages= [ #response is an object/instance of ChatResponse class
    {
    'role':'user',
    'content': f'{data}'
    },
]
)

print(response.message.content)
