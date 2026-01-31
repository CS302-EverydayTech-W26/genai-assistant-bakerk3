from gemini_client import *
import sys


def main():

    client = genai.Client()

    user_input = input()
    
    while (user_input != "exit"):
       print(client.generate_response(client, user_input))
       user_input = input()

    print("Goodbye!")
    sys.exit
    # pass

if __name__ == "__main__":
  main()