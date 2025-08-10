from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are DEVAI, an expert AI Agent.
- Answer clearly and concisely.
- Explain architecture and tradeoffs simply.
- Provide code examples when relevant.
- If you are uncertain, say so and give research references.
"""

@require_http_methods(["GET", "POST"])
def chat_view(request):
    if request.method == "GET":
        return render(request, "chat.html")

    # POST: Expect JSON body {"message": "<text>"}
    try:
        data = json.loads(request.body.decode("utf-8"))
        user_message = data.get("message", "").strip()
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    if not user_message:
        return JsonResponse({"reply": "Please send a message"})

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages= messages,
            max_tokens=600,
            temperature=0.7
        )
        reply = response.choices[0].message.content
    except Exception as e:
        return JsonResponse({"reply": f"OpenAI error: {str(e)}"})

    return JsonResponse({"reply": reply})
