def doc_to_text_naive(doc):
    return "Translate English to Swahili: " + doc["eng"]


def doc_to_text_template(doc):
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
