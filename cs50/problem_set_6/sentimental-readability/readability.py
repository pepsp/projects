import re


def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    level = grade_level(letters, words, sentences)
    if level < 1:
        print("Before Grade 1")
    elif level >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {level}")


def count_letters(n):
    count = 0
    for char in n:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    return len(text.split())


def count_sentences(text):
    sentences = 0
    match = re.finditer(
        r"[.!?]", text
    )
    for _ in match:
        sentences += 1
    return sentences


def grade_level(letters, words, sentences):
    l = float(letters) / words * 100
    s = float(sentences) / words * 100
    index = 0.0588 * l - 0.296 * s - 15.8
    return round(index)


main()
