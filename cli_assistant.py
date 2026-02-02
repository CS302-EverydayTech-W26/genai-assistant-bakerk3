from gemini_client import *
import sys


def main():

    client = GeminiClient()

    print("Type your prompt here:")
    user_input = input()
    
    while (user_input != "exit"):
       print(client.generate_response(user_input))
       print("Type your prompt here:")
       user_input = input()

    print("Goodbye!")
    sys.exit

if __name__ == "__main__":
  main()