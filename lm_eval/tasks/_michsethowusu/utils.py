def doc_to_text(doc):
    english = doc["eng"]
    prompt = (
        "Translate the following English text to Swahili\n"
        "Only provide the translation, do not include any additional text.\n"
        "for example:\n"
        "Input: Hello, how are you?\n"
        "Output: Habari, unaendeleaje?\n"
        f"Input: {english}\n"
        "Output:"
    )
    return prompt
