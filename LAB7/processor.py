"""Bowling alley input processor used for the Lab 7 fuzz-testing exercise."""


def format_player_name(name):
    """Title-case a player name and limit it to the scoreboard's 10 characters."""
    if not isinstance(name, str):
        return ""
    return name.strip().title()[:10]


def parse_frame(text):
    """Parse one bowling frame as a strike (X), spare (7/), or two rolls (45)."""
    if not isinstance(text, str):
        return 0, 0
    text = text.strip().upper()
    if text == "X":
        return 10, 0
    if len(text) != 2 or text[0] not in "0123456789":
        return 0, 0
    first = int(text[0])
    if text[1] == "/":
        return first, 10 - first
    if text[1] not in "0123456789":
        return 0, 0
    second = int(text[1])
    if first + second > 10:
        return 0, 0
    return first, second


def parse_scoreboard(text):
    """Parse comma-separated NAME:SCORE entries into a dictionary."""
    scores = {}
    if not isinstance(text, str):
        return scores
    for entry in text.split(","):
        parts = entry.split(":")
        if len(parts) != 2:
            continue
        name, score = parts[0].strip(), parts[1].strip()
        if not name:
            continue
        try:
            value = int(score)
        except ValueError:
            continue
        if 0 <= value <= 300:
            scores[name] = value
    return scores


def main():
    print("==== Running format_player_name ====")
    value = input("Enter a player name for the scoreboard: ")
    print("Scoreboard name:", format_player_name(value))

    print("\n==== Running parse_frame ====")
    value = input("Enter a frame as X (strike), 7/ (spare) or two digits (e.g. 45): ")
    print("Pins (first roll, second roll):", parse_frame(value))

    print("\n==== Running parse_scoreboard ====")
    value = input("Enter scores as NAME:SCORE separated by commas (e.g. Asha:150,Ravi:132): ")
    print("Scoreboard:", parse_scoreboard(value))


if __name__ == "__main__":
    main()
