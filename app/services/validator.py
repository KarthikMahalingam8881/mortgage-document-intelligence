def has_sufficient_text(text: str):

    MIN_TEXT_LENGTH = 300

    return len(text.strip()) >= MIN_TEXT_LENGTH