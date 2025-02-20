import BirdsOfaFeather
import EndofaBeginning
import Enchanted
import ForeverYoung
import LetItHappen
import Apocalypse
import Surprise

def clear_screen():
    print("\033c", end="") 

def print_melancholic_header():
    print("\n===================================")
    print("         A Journey in Music        ")
    print("       And Animation Awaits        ")
    print("===================================\n")

def display_menu():
    print("Please, take a moment to select a song or animation:\n")
    print("1. Birds of a Feather - An Echo of Freedom")
    print("2. End of Beginning - The Dusk of Time")
    print("3. Enchanted - A Whirl of Dreams")
    print("4. Forever Young - A Flicker of Hope")
    print("5. Let It Happen - Embrace the Unknown")
    print("6. Apocalypse - The Last Dawn")
    print("7. Surprise - A Hidden Reflection")
    print("0. Exit - Fade to Silence\n")

def handle_selection(choice):
    if choice == "1":
        print("\nPlaying 'Birds of a Feather'... A song of freedom, yet bound by the winds of time.\n")
        BirdsOfaFeather.sing_song_main()
    elif choice == "2":
        print("\nPlaying 'End of Beginning'... The quiet solemnity of life's final moments.\n")
        EndofaBeginning.print_lyrics()
    elif choice == "3":
        print("\nAnimating 'Enchanted'... A swirling dream, half remembered.\n")
        Enchanted.enchanted()
    elif choice == "4":
        print("\nAnimating 'Forever Young'... A faint whisper, longing to remain.\n")
        ForeverYoung.forever_young()
    elif choice == "5":
        print("\nAnimating 'Let It Happen'... A quiet acceptance of the inevitable.\n")
        LetItHappen.now_im_ready()
    elif choice == "6":
        print("\nAnimating 'Apocalypse'... The last breath of a world we once knew.\n")
        Apocalypse.apocalypse()
    elif choice == "0":
        print("\nExiting... Let silence take over.\n")
        exit()
    else:
        print("\nThat's not a valid choice. Please, select again.\n")

def main():
    clear_screen()
    while True:
        print_melancholic_header()
        display_menu()
        choice = input("Make your choice: ")
        handle_selection(choice)
        Surprise.main()

if __name__ == "__main__":
    main()
