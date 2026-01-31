from google import genai
from google.genai import types
import os
import sys
import gemini_config as config
    
class GeminiClient:
    def __init__(self):
        gemini_api_key = config.GEMINI_API_KEY
        if gemini_api_key is None:
            print("Your API key is not set correctly!")
            sys.exit()
        else:
            self.client = genai.Client(api_key=gemini_api_key)
            self.chat_history = []

    def generate_response(self, user_input):
        if self.chat_history == None:  
            return "AI Assistant is not configured correctly"
        
        else:
            # TO DO: Modify system instruction based on the purpose of your GenAI Assistant
            # Overarching general instructions, could format output in whatever way you want
            system_instruction = "Please cite your sources, and include an inspirational limerick at the end of your response."
            
            # Add the prompt to the chat history
            self.chat_history += [types.Content(
                  role='user',
                  parts=[types.Part.from_text(text=user_input)]
                )]

            # TO DO: Use the client's chat history & system instruction to prompt Gemini. in documentation there is contents,
            # contents = self.chat_history

            # client = genai.Client()
            client = self

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                config=types.GenerateContentConfig(
                    system_instruction),
                contents=self.chat_history
            )

            chat = client.chats.create(model="gemini-3-flash-preview")

            response = chat.send_message_stream(user_input)

            # TO DO: Add the response text from Gemini to the client's chat history

            self.chat_history += [types.Content(
                  role='user',
                  parts=[types.Part.from_text(text=response)]
                )]

            # TO DO: Return the response text from Gemini

            return self.chat_history