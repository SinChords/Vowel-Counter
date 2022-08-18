def vowel_counter():
    str = input("\nEnter a string: ").lower()
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for letter in str:
        if letter in vowels:
            vowel_count += 1
    if vowel_count == 0:
        print(f"There are no vowels in {str}")
    else:
        print(f"There are {vowel_count} vowels in {str}")
    again = input("\nWould you like to enter another word? Answer y/n.\n").lower()
    if again == "y":
        vowel_counter()

vowel_counter()