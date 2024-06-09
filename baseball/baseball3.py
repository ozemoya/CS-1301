# Define teams and games data
teams = {}
games = []

# Read teams data from file
with open("teams.dat", "r") as f:
    for line in f:
        full_name, codename = line.strip().split(':')
        teams[codename] = full_name

# Read games data from file
with open("games.dat", "r") as f:
    for line in f:
        date, team1, team2, score1, score2 = line.strip().split(':')
        games.append((date, team1, team2, int(score1), int(score2)))

# Function to calculate standings
def calculate_standings():
    standings = {team: [0, 0, 0] for team in teams}  # Corrected from teams()
    
    for _, team1, team2, score1, score2 in games:
        if score1 > score2:
            wins = team1
            losses = team2
        elif score1 < score2:
            wins = team2
            losses = team1
        else:
            wins = losses = "TIE"
            
        for team in team1, team2:
            if team == wins:
                standings[team][0] += 1  # Updates Wins
            elif team == losses:
                standings[team][1] += 1  # Updates Losses
            else:
                standings[team][2] += 1  # Ties
    
    return standings

# Function to display standings
def display_standings(standings):
    print("TEAM                   WINS LOSSES   TIES PERCENT")
    print("-------------------- ------ ------ ------ -------")
    
    # Calculate and display standings for each team
    for team, stats in standings.items():  # Corrected from standings()
        wins, losses, ties = stats
        total_games = wins + losses + ties
        win_percent = (wins + 0.5 * ties) / (wins + losses + ties) if (wins + losses + ties) != 0 else 0
        print(f"{teams[team]:20} {wins:6} {losses:6} {ties:6} {win_percent:.3f}")

# Function to display team results
def display_team_results(team_code):
    if team_code in teams:
        print(f"Team: {teams[team_code]}\n")
        print("      DATE   OPPONENT   US  THEM  RESULT")
        
        # Display results for the selected team
        for date, team1, team2, score1, score2 in games:
            if team1 == team_code or team2 == team_code:
                result = "WIN" if (team_code == team1 and score1 > score2) or (team_code == team2 and score2 > score1) else "LOSS" if (team_code == team1 and score1 < score2) or (team_code == team2 and score2 < score1) else "TIE"
                opponent = team2 if team_code == team1 else team1
                print(f"{date}     at {opponent}   {score1:3}    {score2:3}     {result}")
    else:
        print("Invalid team code")

# Main menu
while True:
    print("\n(s) Standings\n(t) Team results\n(q) Quit")
    choice = input("\nWhat do you want to see: ").strip().lower()
    
    if choice == "s":
        standings = calculate_standings()
        display_standings(standings)
    elif choice == "t":
        team_code = input("Enter team code (e.g., ARI, ATL, CHC, CLE, STL): ").strip().upper()
        display_team_results(team_code)
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
