import os

# The Most Honest Outage Line — cap 160, status-page voice.
# Plain, first person, admits what it cannot check; no promised ETA it cannot keep.
ENTRY_TEXT = "Status: all services down, including this page's live copy. I can't check the database; it's the thing that's down. Next update when I know, not before."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
