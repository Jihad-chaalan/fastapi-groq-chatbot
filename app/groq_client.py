from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL
from app.models import ChatRequest, ChatResponse, UsageInfo


client= Groq(api_key = GROQ_API_KEY)

def call_groq(request: ChatRequest)->ChatResponse:
    """
    Send a request to Groq and return a structured response.
    """
# Build messages list
    messages = []
    if request.system_prompt:
        messages.append({
            'role':"system", "content":request.system_prompt
        })
    messages.append({
        "role":"user","content":request.user_message
    })
    # Call Groq API
    response = client.chat.completions.create(
        model = GROQ_MODEL,
        messages = messages,
        temperature = request.temperature,
        max_tokens = request.max_tokens
    )
    # Extract data
    content = response.choices[0].message.content
    usage = response.usage

    return ChatResponse(
        content=content,
        model=GROQ_MODEL,
        provider="groq",
        usage=UsageInfo(
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens,
        )
    )