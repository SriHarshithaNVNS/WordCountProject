def word_counter(var):
    # This is a method which takes string as input and returns
    # the total number of words as int
    var = var.strip()
    if len(var) > 0:
        wordlist = var.split(" ")
        return len(wordlist)
    return 0


print("Welcome to word counter\nEnter 'bye' to exit!!")

# This is a loop which is True until the input string is "bye"
while True:
    sentence = input("Enter a sentence: ")

    # Conditional statement if the input sentence is bye
    if sentence.lower() == "bye":
        break

    # Calling the function word_counter() by giving the input sentence
    wc = word_counter(sentence)

    # Printing a sentence if the given input is 0
    if wc == 0:
        print("Please enter some text.")

    # Printing number of words
    print("No of words in the given sentence is:", wc)

# Conclusion Prompt
print("=====================================================")
print("                          Bye                      ")
print("=====================================================")
