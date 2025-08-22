import json

# File to save player data
FILENAME = "players.json"

# List to store all players
players = []

# Load players from file if it exists
def load_players():
    global players
    try:
        with open(FILENAME, "r") as file:
            players = json.load(file)
            print("\n📁 Players loaded from file.\n")
    except FileNotFoundError:
        print("\n⚠️ No saved players found. Starting fresh.\n")

# Save players to file
def save_players():
    with open(FILENAME, "w") as file:
        json.dump(players, file, indent=4)
    print("\n💾 Players saved to file.\n")

# Add a new player
def add_player():
    name = input("Enter player name: ").strip()
    while not name:
        name = input("Name can't be empty. Enter player name: ").strip()

    while True:
        try:
            age = int(input("Enter player age: "))
            break
        except ValueError:
            print("Invalid age. Please enter a number.")

    role = input("Enter player role (e.g., Batsman, Bowler): ").strip()
    while not role:
        role = input("Role can't be empty. Enter player role: ").strip()

    player = {"Name": name, "Age": age, "Role": role}
    players.append(player)
    print(f"\n✅ Player '{name}' added successfully!\n")

# View all players
def view_players():
    if not players:
        print("\n⚠️ No players added yet.\n")
        return
    print("\n📋 List of Players:")
    i = 1
    for player in players:
        print(i, ". Name:", player['Name'], ", Age:", player['Age'], ", Role:", player['Role'])
        i += 1
    print()

# Remove a player
def remove_player():
    view_players()
    if not players:
        return
    try:
        choice = int(input("Enter the number of the player to remove: "))
        if 1 <= choice <= len(players):
            removed = players.pop(choice - 1)
            print(f"\n🗑️ Player '{removed['Name']}' removed successfully.\n")
        else:
            print("❌ Invalid player number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Edit a player's details
def edit_player():
    view_players()
    if not players:
        return
    try:
        choice = int(input("Enter the number of the player to edit: "))
        if 1 <= choice <= len(players):
            player = players[choice - 1]
            print(f"Editing '{player['Name']}'")
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_age = input("Enter new age (leave blank to keep current): ").strip()
            new_role = input("Enter new role (leave blank to keep current): ").strip()

            if new_name:
                player['Name'] = new_name
            if new_age.isdigit():
                player['Age'] = int(new_age)
            if new_role:
                player['Role'] = new_role

            print("\n✏️ Player updated successfully.\n")
        else:
            print("❌ Invalid player number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Show basic stats
def show_stats():
    if not players:
        print("\n⚠️ No players added yet.\n")
        return
    total = len(players)
    batsmen = sum(1 for p in players if p['Role'].lower() == 'batsman')
    bowlers = sum(1 for p in players if p['Role'].lower() == 'bowler')
    print(f"\n📊 Total Players: {total} | Batsmen: {batsmen} | Bowlers: {bowlers}\n")

# Select team of 11

def select_team():
    if len(players) < 11:
        print("\n⚠️ Not enough players to select a team (need at least 11).\n")
        return
    print("\nSelect 11 players by entering their numbers (1 to", len(players), ")")
    view_players()

    selected_indices = set()
    while len(selected_indices) < 11:
        try:
            choice = int(input(f"Select player {len(selected_indices)+1}: "))
            if 1 <= choice <= len(players):
                if choice in selected_indices:
                    print("⚠️ Player already selected. Choose a different one.")
                else:
                    selected_indices.add(choice)
            else:
                print("❌ Invalid number. Try again.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")

    print("\n✅ Match Team (Playing XI):")
    i = 1
    for index in selected_indices:
        player = players[index - 1]
        print(i, ". Name:", player['Name'], "- Role:", player['Role'])
        i += 1
    print()

# Main menu
def menu():
    load_players()
    while True:
        print("\n🏏 Cricket Team Management System")
        print("1. Add Player")
        print("2. View Players")
        print("3. Remove Player")
        print("4. Edit Player")
        print("5. Show Stats")
        print("6. Select Team (11 Players)")
        print("7. Save Players")
        print("8. Load Players")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == '1':
            add_player()
        elif choice == '2':
            view_players()
        elif choice == '3':
            remove_player()
        elif choice == '4':
            edit_player()
        elif choice == '5':
            show_stats()
        elif choice == '6':
            select_team()
        elif choice == '7':
            save_players()
        elif choice == '8':
            load_players()
        elif choice == '9':
            print("\n👋 Exiting the program.....")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

# Run the program
menu()
