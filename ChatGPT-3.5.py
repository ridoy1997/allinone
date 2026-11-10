import requests
while True:
    prompt = input("insert prompt: ")
    response = requests.get(url = f"https://www.pyhanzo.com/ChatGPT3.5?prompt={prompt}")
    print(f"\n{response.text}\n")
