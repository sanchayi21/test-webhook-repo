def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a number as currency string."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return f"{currency} {amount:.2f}"

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to max_length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
