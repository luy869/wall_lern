import ollama

client = ollama.Client(host="http://localhost:11434")
response = client.chat(model="qwen3.6:27b", 

options={
    "thinking": True,
    "num_predict": 4096,
    "temperature": 0.2,
    "num_ctx": 8192,
},

messages=[
    {
        'role': 'user',
        'content': 'SCP財団ってしってる？',
    },
])
print(response["message"]["content"])   