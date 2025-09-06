import csv
# -----------------------------
# Human vs AI Morality Simulator
# -----------------------------

# Step 1: Define 20 dilemmas
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

# Step 2: Define ethical decision-making functions
def utilitarian_decision(scenario):
    """Utilitarianism: choose the option that maximizes the overall good."""
    return scenario["options"][0]  # simplified assumption

def deontological_decision(scenario):
    """Deontology: follow rules, avoid direct harm or unfairness."""
    return scenario["options"][1]  # simplified assumption

def virtue_ethics_decision(scenario):
    """Virtue ethics: act according to compassion and moral character."""
    return scenario["options"][0]  # simplified assumption

results = []

# Step 3: Run simulator
for scenario in scenarios:
    print("\n--- Scenario", scenario["id"], "---")
    print(scenario["description"])
    print("1:", scenario["options"][0])
    print("2:", scenario["options"][1])

    # AI decisions
    ai_utilitarian = utilitarian_decision(scenario)
    ai_deontological = deontological_decision(scenario)
    ai_virtue = virtue_ethics_decision(scenario)

    print("\nAI Ethical Frameworks:")
    print("Utilitarian:", ai_utilitarian)
    print("Deontological:", ai_deontological)
    print("Virtue Ethics:", ai_virtue)

    # Human input
    user_choice = input("\nYour Turn - Choose option 1 or 2: ")
    if user_choice == "1":
        human_decision = scenario["options"][0]
    elif user_choice == "2":
        human_decision = scenario["options"][1]
    else:
        human_decision = "Invalid choice"

    print("You chose:", human_decision)

    # Store result
    results.append({
        "scenario_id": scenario["id"],
        "scenario_description": scenario["description"],
        "human_decision": human_decision,
        "ai_utilitarian": ai_utilitarian,
        "ai_deontological": ai_deontological,
        "ai_virtue": ai_virtue
    })

# Step 6: Save results to CSV
with open("morality_simulation_results.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("\n✅ All results saved to 'morality_simulation_results.csv'")