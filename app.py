# app.py
from simulator import scenarios, utilitarian_decision, deontological_decision, virtue_ethics_decision, analyze_results

from flask import Flask, render_template, request, redirect, url_for
import csv
import pandas as pd
from simulator import (
    scenarios,
    utilitarian_decision,
    deontological_decision,
    virtue_ethics_decision,
    analyze_results
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", scenarios=scenarios)

@app.route("/submit", methods=["POST"])
def submit():
    user_id = request.form.get("user_id", "").strip()
    results = []

    for scenario in scenarios:
        choice = request.form.get(f"scenario_{scenario['id']}")
        if choice == "1":
            human_decision = scenario["options"][0]
        elif choice == "2":
            human_decision = scenario["options"][1]
        else:
            human_decision = "Invalid choice"

        ai_utilitarian = utilitarian_decision(scenario)
        ai_deontological = deontological_decision(scenario)
        ai_virtue = virtue_ethics_decision(scenario)

        results.append({
            "user_id": user_id,
            "scenario_id": scenario["id"],
            "scenario_description": scenario["description"],
            "human_decision": human_decision,
            "ai_utilitarian": ai_utilitarian,
            "ai_deontological": ai_deontological,
            "ai_virtue": ai_virtue
        })

    # Save CSV (overwrites same file as CLI)
    if results:
        save_path = "morality_simulation_results.csv"
        with open(save_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

    return redirect(url_for("results_page"))

@app.route("/results")
def results_page():
    csv_path = "morality_simulation_results.csv"
    try:
        df = pd.read_csv(csv_path)
        table_html = df.to_html(classes="table table-bordered w-full", index=False, escape=False)
    except FileNotFoundError:
        df = None
        table_html = "<p>No results saved yet.</p>"

    # Compute accuracy (use corrected encoding — change to preserve_original_encoding=True if you want old behavior)
    acc = analyze_results(csv_path, preserve_original_encoding=False)
    acc_display = f"{acc:.3f}" if acc is not None else "N/A (not enough data)"

    return render_template("results.html", table_html=table_html, accuracy=acc_display)

if __name__ == "__main__":
    app.run(debug=True)
