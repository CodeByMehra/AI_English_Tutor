def clean_transcript(raw_text):
    lowered_text = raw_text.lower()

    splitted_text = lowered_text.split()
    
    cleaned_words = []
    for word in splitted_text:
        if word not in {"um", "uh"} :
            cleaned_words.append(word)

    final_str =""
    for word in cleaned_words:
        final_str = " ".join(cleaned_words)
    return final_str
