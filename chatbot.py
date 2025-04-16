import requests

def chat_with_bot():
    print("🤖 MHC Bot: Hey! I'm here for you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("🤖 MHC Bot: Take care! I'm always here if you need me. 💙")
            break

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"You are a kind and supportive friend who gives emotional support. The user says: {user_input}",
                "stream": False
            }
        )

        reply = response.json()["response"]
        print(f"🤖 MHC Bot: {reply.strip()}")

chat_with_bot()
