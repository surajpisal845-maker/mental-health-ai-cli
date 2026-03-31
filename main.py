import json
import os

# =========================
# Emotion Detection (AI Logic)
# =========================
def detect_emotion(text):
    text = text.lower()

    if "sad" in text or "depressed" in text or "lonely" in text:
        return "Sad "
    elif "happy" in text or "excited" in text or "good" in text:
        return "Happy "
    elif "stress" in text or "exam" in text or "tension" in text:
        return "Stress "
    elif "angry" in text or "frustrated" in text:
        return "Angry "
    else:
        return "Neutral "

# =========================
# Suggestion Engine
# =========================
def give_suggestion(emotion):
    if "Sad" in emotion:
        return "Talk to someone you trust, listen to music, and take rest."
    elif "Happy" in emotion:
        return "Great! Keep doing what makes you happy."
    elif "Stress" in emotion:
        return "Take breaks, make a study plan, and avoid overthinking."
    elif "Angry" in emotion:
        return "Take deep breaths, go for a walk, and stay calm."
    else:
        return "Stay positive and take care of yourself."

# =========================
# Save History (JSON)
# =========================
def save_history(text, emotion, suggestion):
    data = {
        "input": text,
        "emotion": emotion,
        "suggestion": suggestion
    }

    with open("data.json", "a") as file:
        file.write(json.dumps(data) + "\n")

# =========================
# View History
# =========================
def view_history():
    if not os.path.exists("data.json"):
        print("\nNo history found.\n")
        return

    print("\n=== History ===")
    with open("data.json", "r") as file:
        for line in file:
            record = json.loads(line)
            print(f"\nInput: {record['input']}")
            print(f"Emotion: {record['emotion']}")
            print(f"Suggestion: {record['suggestion']}")

# =========================
# Analyze Text
# =========================
def analyze_text():
    text = input("\nEnter your feelings: ").strip()

    if text == "":
        print(" Input cannot be empty!")
        return

    emotion = detect_emotion(text)
    suggestion = give_suggestion(emotion)

    print("\n Detected Emotion:", emotion)
    print(" Suggestion:", suggestion)

    save_history(text, emotion, suggestion)

# =========================
# Help Menu
# =========================
def show_help():
    print("\n=== Help Menu ===")
    print("1 → Analyze your feelings")
    print("2 → View past history")
    print("3 → Exit the program")

# =========================
# Main Menu
# =========================
def show_menu():
    print("\n=== Mental Health AI Assistant ===")
    print("1. Analyze Text")
    print("2. View History")
    print("3. Help")
    print("4. Exit")

# =========================
# MAIN LOOP
# =========================
def main():
    print("Welcome to Mental Health AI Assistant ")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            analyze_text()
        elif choice == "2":
            view_history()
        elif choice == "3":
            show_help()
        elif choice == "4":
            print("\nGoodbye  Stay strong!")
            break
        else:
            print(" Invalid choice! Please try again.")

# Run program
if __name__ == "__main__":
    main()
