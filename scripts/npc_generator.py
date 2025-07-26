import random

def generate_npc_dna(seed=None):
    """
    Generates a complete NPC DNA set, including Personality, Physical, and Naming Style.
    """
    rng = random.Random(seed)

    # --- Part 1: Personality DNA ---
    def generate_personality_dna_string():
        lnc_traits = [
            ("B", "C"), ("R", "O"), ("L", "T"), ("F", "I"), ("S", "X"),
            ("P", "M"), ("D", "U"), ("G", "H"), ("Y", "W"), ("E", "A"),
            ("N", "V"), ("K", "Q"), ("Z", "B"), ("O", "P"), ("C", "H"),
            ("R", "L"), ("A", "S"), ("D", "A"), ("A", "H"), ("I", "C")
        ]
        gne_traits = [
            "H", "C", "K", "G", "L", "J", "M", "F", "E", "B", "U", "S", "I", "R", "T", "A", "D", "V", "Y", "X"
        ]

        lnc_dna_parts, lnc_scores = [], []
        for pair in lnc_traits:
            chosen_trait = rng.choice(pair)
            lnc_score = rng.randint(1, 9)
            intensity = rng.randint(1, 5)
            lnc_scores.append(lnc_score)
            lnc_dna_parts.append(f"{lnc_score}{chosen_trait[0]}{intensity}")

        gne_dna_parts, gne_scores = [], []
        for trait in gne_traits:
            gne_score = rng.randint(1, 9)
            gne_scores.append(gne_score)
            gne_dna_parts.append(f"{trait[0]}{gne_score}")

        lnc_average = round(sum(lnc_scores) / len(lnc_scores))
        gne_average = round(sum(gne_scores) / len(gne_scores))

        return f"({lnc_average}/{gne_average}) {','.join(lnc_dna_parts)} - {','.join(gne_dna_parts)}"

    # --- Part 2: Physical DNA ---
    def generate_physical_dna_string():
        physical_gene_map = [
            ('R', 8),  # Race/Origin
            ('A', 6),  # Age Category
            ('B', 5),  # Build/Physique
            ('F', 7),  # Distinguishing Feature
            ('E', 6),  # Equipment Style
        ]
        physical_parts = []
        for letter, count in physical_gene_map:
            value = rng.randint(1, count)
            physical_parts.append(f"{letter}{value}")
        return "".join(physical_parts)

    # --- Part 3: Naming Style DNA ---
    def generate_naming_style_dna_string():
        naming_style_value = rng.randint(1, 5)
        return f"NS{naming_style_value}"

    return {
        "personality_dna": generate_personality_dna_string(),
        "physical_dna": generate_physical_dna_string(),
        "naming_style_dna": generate_naming_style_dna_string()
    }

if __name__ == "__main__":
    dna = generate_npc_dna()
    print(f"{dna['personality_dna']}|{dna['physical_dna']}|{dna['naming_style_dna']}")
