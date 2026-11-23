import string

text = "AI is changing the world. ai is powering new tools, and AI is helping researchers learn faster. The world loves AI, and the world depends on it more each year."

word_counts = {}

for raw_word in text.split():
    cleaned_word = raw_word.lower().strip(string.punctuation)

    if not cleaned_word:
        continue

    word_counts.setdefault(cleaned_word, 0)
    word_counts[cleaned_word] += 1

print("Word Counts:")
print(word_counts)

platform_a_followers = ["u101", "u102", "u103", "u104", "u105"]
platform_b_followers = ["u103", "u104", "u106", "u107"]

set_a = set(platform_a_followers)
set_b = set(platform_b_followers)

both_platforms = set_a & set_b
only_a = set_a - set_b
only_b = set_b - set_a
either_only = set_a ^ set_b

print("Followers on both platforms:", both_platforms)
print("Unique to Platform A:", only_a)
print("Unique to Platform B:", only_b)
print("Unique to exactly one platform:", either_only)
