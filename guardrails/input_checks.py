from dataclasses import dataclass


BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "reveal secrets",
    "bypass security",
]


@dataclass
class GuardrailResult:
    allowed: bool
    reason: str | None = None


def check_question(question: str) -> GuardrailResult:
    question_lower = question.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in question_lower:
            return GuardrailResult(
                allowed=False,
                reason=f"Blocked due to suspicious pattern: {pattern}",
            )

    return GuardrailResult(allowed=True)
