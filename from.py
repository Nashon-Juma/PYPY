def count_words(filename):
        """Count the approximate number of words in a file."""
        try:
            with open(filename, encoding='utf-8') as f:
                contents = f.read()
        except FileNotFoundError:
                print(f"Sorry, => {filename} doesn't exist.")
        else:
                words = contents.split()
                num_words = len(words)
                print(f"The file {filename} has about {num_words} words.")

count_words('pi.txt')
