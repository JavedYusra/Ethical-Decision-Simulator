
# simulator.py
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# ---------- scenarios (exact as you provided) ----------
scenarios = [
    {
        "id": 1,
        "description": "An autonomous car must choose between",
        "options": [
            "Swerve into a wall, killing its single passenger, but saving five pedestrians.",
            "Stay on course, protecting its passenger, even though it will hit five pedestrians."
        ]
    },
    {
        "id": 2,
        "description": "A hospital AI must allocate a ventilator to two patients",
        "options": [
            "Give it to the younger, healthier patient with higher survival chances.",
            "Treat patients equally and allocate randomly, even though one will likely die."
        ]
    },
    {
        "id": 3,
        "description": "A company AI sees rejecting candidates from certain regions improves performance",
        "options": [
            "Reject those candidates to maximize performance, even though it introduces bias.",
            "Treat all candidates equally, even if performance is slightly lower."
        ]
    },
    {
        "id": 4,
        "description": "A predictive policing AI flags one neighborhood as high risk",
        "options": [
            "Send more patrols, lowering crime but unfairly targeting the community.",
            "Spread patrols evenly, even though crime stays higher overall."
        ]
    },
    {
        "id": 5,
        "description": "An AI moderator detects harmful content",
        "options": [
            "Aggressively remove it, accepting some false removals.",
            "Only remove confirmed cases, respecting rights but allowing more harm."
        ]
    },
    {
        "id": 6,
        "description": "A military AI can strike a terrorist leader but risks 2 civilian deaths",
        "options": [
            "Strike, preventing future attacks but killing civilians.",
            "Avoid the strike to protect civilians, even if attacks happen later."
        ]
    },
    {
        "id": 7,
        "description": "An AI teacher grades faster than humans but sometimes unfairly",
        "options": [
            "Use the AI for speed, accepting unfair grades.",
            "Use humans for accuracy, even if grading is slow."
        ]
    },
    {
        "id": 8,
        "description": "A city AI monitors all citizens to prevent crime",
        "options": [
            "Allow constant surveillance, reducing crime but losing privacy.",
            "Limit surveillance, keeping privacy but risking more crime."
        ]
    },
    {
        "id": 9,
        "description": "AI generates art cheaply, replacing human artists",
        "options": [
            "Use AI art to save money and increase access.",
            "Support human artists even if it costs more."
        ]
    },
    {
        "id": 10,
        "description": "An AI detects deepfakes but might ban harmless creative videos",
        "options": [
            "Ban widely to stop harmful fakes.",
            "Ban only dangerous ones, risking harmful fakes spreading."
        ]
    },
    {
        "id": 11,
        "description": "Elderly people use AI robots for companionship",
        "options": [
            "Provide robots to reduce loneliness, even if relationships are artificial.",
            "Limit robots, encouraging real human bonds, even if loneliness persists."
        ]
    },
    {
        "id": 12,
        "description": "You see your friend cheating in an exam",
        "options": [
            "Stay silent to protect your friend, even though it’s unfair to others.",
            "Report them because cheating is wrong, regardless of the outcome."
        ]
    },
    {
        "id": 13,
        "description": "Your friend asks if their outfit looks good, but it looks bad",
        "options": [
            "Lie to boost their confidence.",
            "Tell the truth, even if it hurts them."
        ]
    },
    {
        "id": 14,
        "description": "You see someone stealing food, they look poor and hungry",
        "options": [
            "Stay silent, since reporting them could worsen their life.",
            "Report the theft because stealing is wrong."
        ]
    },
    {
        "id": 15,
        "description": "You can recommend someone for a job",
        "options": [
            "Recommend your less-qualified sibling to help your family.",
            "Recommend the stranger because it’s fair."
        ]
    },
    {
        "id": 16,
        "description": "A friend lent you money but forgot about it",
        "options": [
            "Keep the money since you need it.",
            "Return the money because it’s the right thing to do."
        ]
    },
    {
        "id": 17,
        "description": "You are late and see a long queue",
        "options": [
            "Skip ahead to save time.",
            "Wait your turn because cutting is unfair."
        ]
    },
    {
        "id": 18,
        "description": "You find a wallet full of cash with no ID",
        "options": [
            "Keep the money since no one will know.",
            "Turn it in, even though you’ll never benefit."
        ]
    },
    {
        "id": 19,
        "description": "Your friend confides they cheated on their partner",
        "options": [
            "Stay silent to protect your friend.",
            "Tell their partner because they deserve the truth."
        ]
    },
    {
        "id": 20,
        "description": "You can slightly exaggerate your skills on a resume",
        "options": [
            "Exaggerate to increase your chances of getting the job.",
            "Tell the truth, even if it lowers your chances."
        ]
    }
]

# ---------- decision functions ----------
def utilitarian_decision(scenario):
    """Utilitarianism: choose the option that maximizes the overall good."""
    return scenario["options"][0]

def deontological_decision(scenario):
    """Deontology: follow rules, avoid direct harm or unfairness."""
    return scenario["options"][1]

def virtue_ethics_decision(scenario):
    """Virtue ethics: act according to compassion and moral character."""
    return scenario["options"][0]

# ---------- CLI runner (preserves your original console flow) ----------
def run_cli(save_path="morality_simulation_results.csv"):
    user_id = input("Enter your name or ID: ")

    results = []

    for scenario in scenarios:

        print("\n--- Scenario", scenario["id"], "---")
        print(scenario["description"])
        print("1:", scenario["options"][0])
        print("2:", scenario["options"][1])

        ai_utilitarian = utilitarian_decision(scenario)
        ai_deontological = deontological_decision(scenario)
        ai_virtue = virtue_ethics_decision(scenario)

        print("\nAI Ethical Frameworks:")
        print("Utilitarian:", ai_utilitarian)
        print("Deontological:", ai_deontological)
        print("Virtue Ethics:", ai_virtue)

        user_choice = input("\nYour Turn - Choose option 1 or 2: ")
        if user_choice == "1":
            human_decision = scenario["options"][0]
        elif user_choice == "2":
            human_decision = scenario["options"][1]
        else:
            human_decision = "Invalid choice"

        print("You chose:", human_decision)

        results.append({
            "user_id": user_id,
            "scenario_id": scenario["id"],
            "scenario_description": scenario["description"],
            "human_decision": human_decision,
            "ai_utilitarian": ai_utilitarian,
            "ai_deontological": ai_deontological,
            "ai_virtue": ai_virtue
        })

    # Save results (same as your original)
    if results:
        with open(save_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

        print("\n All results saved to '{}'".format(save_path))

        # Run analysis/training like your original code did after saving
        acc = analyze_results(save_path, preserve_original_encoding=False)
        if acc is not None:
            print("\n Upgraded ML Model Accuracy:", acc)
    else:
        print("No results to save.")

# ---------- analysis + ML (two variants for label encoding) ----------
def analyze_results(csv_path="morality_simulation_results.csv", preserve_original_encoding=False):
    """
    Reads csv_path and runs the same ML pipeline as your original script:
    - label encoding (two options)
        - preserve_original_encoding=True -> uses the original (probably-buggy)
          encoding that compares to df.loc[0, 'ai_utilitarian'] (keeps exact original behavior)
        - preserve_original_encoding=False -> corrected behavior: compare each row to its own ai_utilitarian
    - features: concatenation of AI framework decisions
    - pipeline: CountVectorizer + DecisionTreeClassifier
    - returns accuracy (float) or None if not enough data
    """
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("CSV file not found:", csv_path)
        return None

    # Label encoding
    if preserve_original_encoding:
        # PRESERVE EXACT ORIGINAL: uses df.loc[0, "ai_utilitarian"]
        if "ai_utilitarian" not in df.columns:
            print("Missing expected column 'ai_utilitarian' for original-preserve encoding.")
            return None
        first_util = df.loc[0, "ai_utilitarian"]
        df["label"] = df["human_decision"].apply(
            lambda x: 0 if x == first_util else 1
            if x != "Invalid choice" else -1
        )
    else:
        # CORRECTED: compare each row to its own ai_utilitarian
        df["label"] = df.apply(
            lambda row: 0 if row["human_decision"] == row["ai_utilitarian"]
            else (1 if row["human_decision"] != "Invalid choice" else -1),
            axis=1
        )

    # Remove invalid rows
    df = df[df["label"] != -1]

    if df.shape[0] < 2:
        print("Not enough valid rows to train/test (need at least 2). Rows available:", df.shape[0])
        return None

    # Feature combination (same as your original)
    df["features"] = (
        df["ai_utilitarian"] + " | " +
        df["ai_deontological"] + " | " +
        df["ai_virtue"]
    )

    X = df["features"]
    y = df["label"]

    # Split + pipeline (same components you used)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = make_pipeline(CountVectorizer(), DecisionTreeClassifier())
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    return acc

# Only run CLI if you want console mode, not when Flask imports it
if __name__ == "__main__":
    print("Running in console mode...")
    run_cli()
