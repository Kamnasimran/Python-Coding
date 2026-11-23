def search4letters(phrase: str, letters="ATCG"):
    return set(letters).intersection(set(phrase.upper()))
