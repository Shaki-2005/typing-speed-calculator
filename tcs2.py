import time

def main():
    test_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence as fast and accurately as you can:\n")
    print(f">>> {test_text}\n")  # Display the sentence to be typed

    # Prompt the user to start
    input("Press Enter when you're ready to start...")

    # Start the timer
    start_time = time.time()

    # Get the user's input
    typed_text = input("\nStart typing: ")

    # End the timer
    end_time = time.time()

    # Calculate time taken to type
    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)

    # Calculate words per minute (WPM)
    word_count = len(typed_text.split())
    wpm = round((word_count / time_taken) * 60)

    # Calculate accuracy
    correct_chars = 0
    for i in range(min(len(test_text), len(typed_text))):
        if test_text[i] == typed_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(test_text)) * 100
    accuracy = round(accuracy, 2)

    # Show the results
    print("\n--- Results ---")
    print(f"Time taken: {time_taken} seconds")
    print(f"Your typing speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    main()

typed_text = input("\nStart typing: ")
input("Press Enter to exit...")  # This will keep the terminal open
print("Program started...")
input("Press Enter when you're ready to start typing...")
print("Ready to take input!")

