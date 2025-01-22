from fpdf import FPDF

class CheatSheet(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Learn German Fast: Cheat Sheet", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", size=10)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_fast_learning_cheat_sheet(output_file):
    pdf = CheatSheet()
    pdf.add_page()

    # Add sections
    pdf.add_section(
        "Basic Greetings and Phrases",
        "Hello: Hallo\n"
        "Good morning: Guten Morgen\n"
        "Good evening: Guten Abend\n"
        "Goodbye: Auf Wiedersehen\n"
        "Please: Bitte\n"
        "Thank you: Danke\n"
        "You're welcome: Gern geschehen\n"
        "Yes: Ja\n"
        "No: Nein\n"
        "Excuse me: Entschuldigung\n"
        "How are you?: Wie geht's?\n"
        "I'm fine, thank you: Mir geht's gut, danke\n"
    )

    pdf.add_section(
        "Numbers (1-10)",
        "1: eins\n"
        "2: zwei\n"
        "3: drei\n"
        "4: vier\n"
        "5: fünf\n"
        "6: sechs\n"
        "7: sieben\n"
        "8: acht\n"
        "9: neun\n"
        "10: zehn"
    )

    pdf.add_section(
        "Days of the Week",
        "Monday: Montag\n"
        "Tuesday: Dienstag\n"
        "Wednesday: Mittwoch\n"
        "Thursday: Donnerstag\n"
        "Friday: Freitag\n"
        "Saturday: Samstag\n"
        "Sunday: Sonntag"
    )

    pdf.add_section(
        "Months of the Year",
        "January: Januar\n"
        "February: Februar\n"
        "March: März\n"
        "April: April\n"
        "May: Mai\n"
        "June: Juni\n"
        "July: Juli\n"
        "August: August\n"
        "September: September\n"
        "October: Oktober\n"
        "November: November\n"
        "December: Dezember"
    )

    pdf.add_section(
        "Common Verbs",
        "To be: sein\n"
        "To have: haben\n"
        "To go: gehen\n"
        "To come: kommen\n"
        "To do/make: machen\n"
        "To eat: essen\n"
        "To drink: trinken\n"
        "To speak: sprechen\n"
        "To work: arbeiten\n"
        "To live: wohnen"
    )

    pdf.add_section(
        "Essential Grammar Tips",
        "1. Articles:\n"
        "   - der (masculine), die (feminine), das (neuter)\n\n"
        "2. Sentence structure:\n"
        "   - Subject -> Verb -> Object: Ich lerne Deutsch (I learn German).\n\n"
        "3. Plurals:\n"
        "   - No fixed rule, memorize common patterns (e.g., -e, -er, -n).\n\n"
        "4. Questions:\n"
        "   - Verb comes first: Sprichst du Deutsch? (Do you speak German?)\n\n"
        "5. Modal Verbs:\n"
        "   - Example: Ich kann Deutsch sprechen (I can speak German)."
    )

    pdf.add_section(
        "Quick Conversation Example",
        "Person A: Hallo! Wie heißt du? (Hello! What's your name?)\n"
        "Person B: Ich heiße Maria. Und du? (My name is Maria. And you?)\n"
        "Person A: Ich heiße Paul. Wie geht's dir? (My name is Paul. How are you?)\n"
        "Person B: Mir geht's gut, danke! (I'm fine, thank you!)"
    )

    # Save the PDF
    pdf.output(output_file)
    print(f"Cheat sheet saved to {output_file}")

if __name__ == "__main__":
    output_file = "Learn_German_Fast_Cheat_Sheet.pdf"
    generate_fast_learning_cheat_sheet(output_file)
