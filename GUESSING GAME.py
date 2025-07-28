import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Input number of players
while True:
    try:
        num_players = int(input("Enter number of players: "))
        if num_players < 1:
            print(" Number of players must be at least 1.")
            continue
        break
    except ValueError:
        print(" Please enter a valid number.")

# Input player names
player_names = []
for i in range(num_players):
    name = input(f"Enter name of Player {i+1}: ").strip()
    player_names.append(name if name else f"Player{i+1}")

# Input number of rounds
while True:
    try:
        num_rounds = int(input("Enter number of rounds: "))
        if num_rounds < 1:
            print(" Number of rounds must be at least 1.")
            continue
        break
    except ValueError:
        print(" Please enter a valid number.")

# Initialize players
players = [{
    "name": name,
    "total_guesses": 0,
    "last_round_guesses": 0
} for name in player_names]

round_results = []
leaderboard_history = []

# Game logic
for round_num in range(1, num_rounds + 1):
    print(f"\n=====  Round {round_num} =====")
    round_guesses = []

    for player in players:
        secret_number = random.randint(1, 100)
        guesses = 0

        while True:
            try:
                guess = int(input(f"{player['name']}, guess the number (1-100): "))
                guesses += 1
                if guess < secret_number:
                    print(" Higher number please!")
                elif guess > secret_number:
                    print(" Lower number please!")
                else:
                    print(f" Correct! It was {secret_number}.")
                    break
            except ValueError:
                print(" Invalid input. Please enter a number.")

        player["total_guesses"] += guesses
        player["last_round_guesses"] = guesses
        round_guesses.append(guesses)

    round_results.append(round_guesses)
    leaderboard_history.append([p["total_guesses"] for p in players])  # for animation

    # Live leaderboard
    print("\n Live Leaderboard:")
    sorted_players = sorted(players, key=lambda x: x["total_guesses"])
    print(f"{'Rank':<5}{'Name':<15}{'Guesses'}")
    for i, p in enumerate(sorted_players):
        print(f"{i+1:<5}{p['name']:<15}{p['total_guesses']}")

# Final scorecard
print("\n Final Scorecard:")
print(f"{'Name':<15}{'Total Guesses'}")
for p in players:
    print(f"{p['name']:<15}{p['total_guesses']}")

# Winner logic
min_guesses = min(p["total_guesses"] for p in players)
winners = [p for p in players if p["total_guesses"] == min_guesses]

if len(winners) == 1:
    print(f"\n Winner: {winners[0]['name']} with {winners[0]['total_guesses']} guesses!")
else:
    best_last = min(p["last_round_guesses"] for p in winners)
    final_winners = [p for p in winners if p["last_round_guesses"] == best_last]
    if len(final_winners) == 1:
        print(f"\n Winner (tie-breaker): {final_winners[0]['name']}")
    else:
        print("\n It's a tie between:")
        for p in final_winners:
            print(f"- {p['name']}")

# --- Charts using Pandas and Matplotlib ---

round_df = pd.DataFrame(round_results, columns=player_names, index=[f"Round {i+1}" for i in range(num_rounds)]).T

# Plot guesses per round
round_df.T.plot(kind='bar', figsize=(12, 6))
plt.title("Guesses per Round per Player")
plt.xlabel("Round")
plt.ylabel("Guesses")
plt.legend(title="Player", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Plot total guesses
summary_df = pd.DataFrame(players)
plt.figure(figsize=(10, 5))
plt.bar(summary_df["name"], summary_df["total_guesses"], color='skyblue')
plt.title("Total Guesses by Each Player")
plt.xlabel("Player")
plt.ylabel("Total Guesses")
plt.tight_layout()
plt.show()

# ---  Pie Chart of Winning Percent (Lower = Better) ---
total_sum = sum([1 / p["total_guesses"] for p in players])
winning_percent = [(1 / p["total_guesses"]) / total_sum * 100 for p in players]
labels = [p["name"] for p in players]

plt.figure(figsize=(8, 6))
plt.pie(winning_percent, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Winning Percentage by Guess Accuracy")
plt.tight_layout()
plt.show()

# ---  Animated Leaderboard Over Rounds ---

fig, ax = plt.subplots(figsize=(10, 6))
bar_container = ax.bar(player_names, leaderboard_history[0], color='orange')
ax.set_ylim(0, max(max(row) for row in leaderboard_history) + 10)
ax.set_title("Leaderboard Progression by Total Guesses")
ax.set_ylabel("Total Guesses")

def update(frame):
    for bar, new_height in zip(bar_container, leaderboard_history[frame]):
        bar.set_height(new_height)
    ax.set_title(f"Leaderboard After Round {frame+1}")
    return bar_container

ani = FuncAnimation(fig, update, frames=len(leaderboard_history), repeat=False, interval=1500)
plt.tight_layout()
plt.show()