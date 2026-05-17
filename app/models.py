from pydantic import BaseModel, Field

# ---------- Request Model ----------
class ChatRequest(BaseModel):
    user_message: str = Field(
        ...,
        description="The user's input message to the chatbot"
    )
    system_prompt: str | None = Field(
        default=None,
        description="Optional system prompt to set assistant behavior"
    )
    temperature: float = Field(
        default=0.7,
        ge=0,
        le=2,
        description="Creativity of the answers (0 = deterministic, 2 = very creative)"
    )
    max_tokens: int = Field(
        default=500,
        le=2000,
        description="Maximum number of tokens in the model's response"
    )

# ---------- Nested Usage Model ----------
class UsageInfo(BaseModel):
    prompt_tokens: int = Field(
        ...,
        ge=0,
        description="Number of tokens in the input prompt"
    )
    completion_tokens: int = Field(
        ...,
        ge=0,
        description="Number of tokens in the generated completion"
    )
    total_tokens: int = Field(
        ...,
        ge=0,
        description="Total tokens used (prompt + completion)"
    )

# ---------- Response Model ----------
class ChatResponse(BaseModel):
    content: str = Field(
        ...,
        description="Model-generated response text"
    )
    model: str = Field(
        ...,
        description="Model identifier used (e.g., 'llama3-70b-8192')"
    )
    provider: str = Field(
        ...,
        description="Model provider (e.g., 'groq')"
    )
    usage: UsageInfo = Field(
        ...,
        description="Token usage information"
    )