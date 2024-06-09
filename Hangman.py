import sys
from PhraseBank import PhraseBank

def play_one_round(phrase):
    remaining_letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ".split()
    guessed_phrase = replace_by_stars(phrase)
    wrong_guesses = 0

    while wrong_guesses < 5 and '*' in guessed_phrase:
        print(f"The current phrase is {guessed_phrase}")
        print("The letters you have not guessed yet are:")
        print(' '.join(remaining_letters))
        guess = get_valid_guess(remaining_letters)
        remaining_letters.remove(guess)

        if guess in phrase.upper():
            guessed_phrase = update_guessed_phrase(phrase, guessed_phrase, guess)
        else:
            wrong_guesses += 1

        print(f"You have made {wrong_guesses} wrong guesses.")
    
    test_if_win_or_loss(phrase, guessed_phrase)

def replace_by_stars(phrase):
    return ''.join(['*' if c.isalpha() else c for c in phrase])

def update_guessed_phrase(phrase, guessed_phrase, guess):
    return ''.join([guess if phrase[i].upper() == guess else guessed_phrase[i] for i in range(len(phrase))])

def test_if_win_or_loss(phrase, guessed_phrase):
    if '*' in guessed_phrase:
        print(f"You lose. The secret phrase was {phrase}")
    else:
        print("YOU WIN!!!!")

def get_valid_guess(remaining_letters):
    guess = ''
    while True:
        guess = input("Enter your next guess: ").upper()
        if guess in remaining_letters:
            return guess
        else:
            print(f"{guess} is not a valid guess.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Hangman.py [phrases file]")
        sys.exit(1)

    phrase_bank = PhraseBank(sys.argv[1])
    topics = phrase_bank.get_all_topics()

    print("This program plays the game of hangman.")
    print("The computer will pick a random phrase.")
    print("After 5 wrong guesses you lose.")
    
    while True:
        print("Please choose a topic")
        for i, topic in enumerate(topics):
            print(f"\t({i}) {topic}")

        topic_index = int(input("Enter topic number (0,1,...): "))
        topic = topics[topic_index]
        phrase = phrase_bank.next_phrase(topic)
        print(f"I am thinking of a {topic} ...")

        play_one_round(phrase)

        if input("Do you want to play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
