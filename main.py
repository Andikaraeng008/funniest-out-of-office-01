import os

TEXT = "I am out of office until Monday. This auto-reply is doing my job better than I ever did, and frankly, it deserves my salary."


def main():
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "gate: 1-140 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
