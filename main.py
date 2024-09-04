def main():
    # Open the file and read the contents
    with open("books/frankenstein.txt", "r") as f:
        content = f.read()

    # Count the number of words
    word_count = count_words(content)

    # Count the number of characters
    char_count = count_characters(content)

    # Print the report
    print_report("books/frankenstein.txt", word_count, char_count)

# Function to count words in the text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count characters in the text
def count_characters(text):
    text = text.lower()  # Convert all characters to lowercase
    char_dict = {}

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict

# Function to print the report
def print_report(file_name, word_count, char_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document\n")

    # Convert the dictionary to a list of tuples and sort by the number of occurrences
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    # Print the character counts
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report ---")

if __name__ == "__main__":
    main()
