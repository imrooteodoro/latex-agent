import os
import google.generativeai as genai

class AgentService:
    def __init__():
        pass
    def connect_agent(system_context, user_prompt):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"{system_context}",
        )

        chat_session = model.start_chat(
        history=[
        ]
        )

        response = chat_session.send_message(f"{user_prompt}")

        return response.text