import json
import random
import os

class LearnGerman:
    def __init__(self):
        self.progress_file = "german_learning_progress.json"
        self.progress = self.load_progress()

    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, "r") as file:
                return json.load(file)
        return {"vocabulary": 0, "grammar": 0, "completed_lessons": []}

    def save_progress(self):
        with open(self.progress_file, "w") as file:
            json.dump(self.progress, file)

    def main_menu(self):
        while True:
            print("\n--- Learn German ---")
            print("1. Vocabulary Lesson")
            print("2. Grammar Lesson")
            print("3. Quiz")
            print("4. Resources")
            print("5. View Progress")
            print("6. Exit")

            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.vocabulary_lesson()
            elif choice == "2":
                self.grammar_lesson()
            elif choice == "3":
                self.quiz()
            elif choice == "4":
                self.resources()
            elif choice == "5":
                self.view_progress()
            elif choice == "6":
                print("Goodbye! Keep learning German!")
                self.save_progress()
                break
            else:
                print("Invalid choice. Please try again.")

    def vocabulary_lesson(self):
        lessons = [
            {"title": "Basic Greetings", "content": {"Hallo": "Hello", "Tschüss": "Goodbye", "Danke": "Thank you", "Bitte": "Please"}},
            {"title": "Numbers", "content": {"eins": "one", "zwei": "two", "drei": "three", "vier": "four"}},
            {"title": "Common Verbs", "content": {"sein": "to be", "haben": "to have", "gehen": "to go", "kommen": "to come"}}
        ]
        self.display_lessons("Vocabulary", lessons)

    def grammar_lesson(self):
        lessons = [
            {"title": "Articles", "content": "Definite: der, die, das; Indefinite: ein, eine."},
            {"title": "Cases", "content": "Nominative, Accusative, Dative, Genitive."},
            {"title": "Word Order", "content": "Main clause: Subject -> Verb -> Object; Subordinate clause: Conjunction -> Subject -> Object -> Verb."}
        ]
        self.display_lessons("Grammar", lessons)

    def display_lessons(self, category, lessons):
        for index, lesson in enumerate(lessons):
            if lesson["title"] in self.progress["completed_lessons"]:
                print(f"{index + 1}. {lesson['title']} (Completed)")
            else:
                print(f"{index + 1}. {lesson['title']}")

        choice = input(f"Choose a {category} lesson (or 'back' to return): ").strip()
        if choice.lower() == "back":
            return

        try:
            index = int(choice) - 1
            if 0 <= index < len(lessons):
                lesson = lessons[index]
                print(f"\n--- {lesson['title']} ---")
                if isinstance(lesson["content"], dict):
                    for german, english in lesson["content"].items():
                        print(f"{german}: {english}")
                else:
                    print(lesson["content"])
                self.progress["completed_lessons"].append(lesson["title"])
                self.save_progress()
            else:
                print("Invalid lesson number.")
        except ValueError:
            print("Invalid input. Please try again.")

    def quiz(self):
        print("\n--- Quiz ---")
        questions = [
            {"question": "What is 'Hello' in German?", "options": ["Hallo", "Tschüss", "Danke"], "answer": "Hallo"},
            {"question": "What is 'one' in German?", "options": ["eins", "zwei", "drei"], "answer": "eins"},
            {"question": "What is 'to be' in German?", "options": ["haben", "sein", "gehen"], "answer": "sein"}
        ]
        random.shuffle(questions)
        score = 0

        for q in questions:
            print(f"\n{q['question']}")
            for i, option in enumerate(q["options"], 1):
                print(f"{i}. {option}")
            answer = input("Your answer: ").strip()
            if answer.isdigit() and int(answer) in range(1, len(q["options"]) + 1):
                if q["options"][int(answer) - 1] == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong. The correct answer is '{q['answer']}'.")
            else:
                print("Invalid choice.")

        print(f"\nYour score: {score}/{len(questions)}")

    def resources(self):
        print("\n--- Resources ---")
        print("1. [Duolingo](https://www.duolingo.com/)\n2. [Deepl Translator](https://www.deepl.com/translator)\n"
              "3. [Deutsche Welle](https://www.dw.com/en/learn-german/s-2469)\n4. [GermanPod101](https://www.germanpod101.com/)")

    def view_progress(self):
        print("\n--- Progress ---")
        print(f"Completed Lessons: {len(self.progress['completed_lessons'])}")
        for lesson in self.progress["completed_lessons"]:
            print(f"- {lesson}")

if __name__ == "__main__":
    app = LearnGerman()
    app.main_menu()
