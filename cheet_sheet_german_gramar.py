from fpdf import FPDF

class GrammarCheatSheet(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "German Grammar Cheat Sheet", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", size=10)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_cheat_sheet(output_file):
    pdf = GrammarCheatSheet()
    pdf.add_page()

    # Add sections
    pdf.add_section(
        "Articles",
        "Definite Articles:\n"
        "  - der (masculine)\n"
        "  - die (feminine)\n"
        "  - das (neuter)\n\n"
        "Indefinite Articles:\n"
        "  - ein (masculine/neuter)\n"
        "  - eine (feminine)\n"
    )

    pdf.add_section(
        "Noun Plurals",
        "1. Add '-e': der Hund -> die Hunde\n"
        "2. Add '-er': das Kind -> die Kinder\n"
        "3. Add '-n' or '-en': die Frau -> die Frauen\n"
        "4. Add '-s': das Auto -> die Autos\n"
        "5. Change vowel (umlaut): der Mann -> die Männer"
    )

    pdf.add_section(
        "Cases",
        "1. Nominative (subject): Wer? Was?\n"
        "   - der Mann, die Frau, das Kind\n\n"
        "2. Accusative (direct object): Wen? Was?\n"
        "   - den Mann, die Frau, das Kind\n\n"
        "3. Dative (indirect object): Wem?\n"
        "   - dem Mann, der Frau, dem Kind\n\n"
        "4. Genitive (possession): Wessen?\n"
        "   - des Mannes, der Frau, des Kindes"
    )

    pdf.add_section(
        "Pronouns",
        "Personal Pronouns:\n"
        "  - ich, du, er/sie/es, wir, ihr, sie/Sie\n\n"
        "Possessive Pronouns:\n"
        "  - mein, dein, sein/ihr/sein, unser, euer, ihr/Ihr"
    )

    pdf.add_section(
        "Verb Conjugation",
        "1. Regular Verbs (spielen - to play):\n"
        "   - ich spiele, du spielst, er/sie/es spielt\n"
        "   - wir spielen, ihr spielt, sie/Sie spielen\n\n"
        "2. Irregular Verbs (fahren - to drive):\n"
        "   - ich fahre, du fährst, er/sie/es fährt\n"
        "   - wir fahren, ihr fahrt, sie/Sie fahren\n\n"
        "3. Modal Verbs:\n"
        "   - können (can), dürfen (may), müssen (must), sollen (should), wollen (want)"
    )

    pdf.add_section(
        "Word Order",
        "1. Main Clause:\n"
        "   - Subject -> Verb -> Object\n"
        "   - Ich kaufe ein Buch.\n\n"
        "2. Subordinate Clause:\n"
        "   - Conjunction -> Subject -> Object -> Verb\n"
        "   - Weil ich ein Buch kaufe.\n\n"
        "3. Question:\n"
        "   - Verb -> Subject -> Object\n"
        "   - Kaufst du ein Buch?"
    )

    pdf.add_section(
        "Adjective Endings",
        "1. With Definite Article:\n"
        "   - der gute Mann, die schöne Frau, das kleine Kind\n\n"
        "2. With Indefinite Article:\n"
        "   - ein guter Mann, eine schöne Frau, ein kleines Kind\n\n"
        "3. Without Article:\n"
        "   - guter Mann, schöne Frau, kleines Kind"
    )

    # Save the PDF
    pdf.output(output_file)
    print(f"Cheat sheet saved to {output_file}")

if __name__ == "__main__":
    output_file = "German_Grammar_Cheat_Sheet.pdf"
    generate_cheat_sheet(output_file)
