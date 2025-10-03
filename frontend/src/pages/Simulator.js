import React, { useState } from "react";

export default function Simulator() {
  const [scenario, setScenario] = useState("");
  const [response, setResponse] = useState("");

  const handleSimulate = () => {
    // Mock response for now
    if (scenario.trim() === "") {
      setResponse("⚠️ Please enter a scenario first.");
    } else {
      setResponse(
        "🤖 AI’s Ethical Decision: In this case, it’s best to act with honesty, fairness, and empathy."
      );
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6">
      <h1 className="text-3xl font-bold mb-6">Ethical Decision Simulator</h1>
      
      <textarea
        className="w-full max-w-lg h-32 border rounded-lg p-4 focus:ring-2 focus:ring-blue-400 text-gray-800"
        placeholder="Enter your ethical dilemma here..."
        value={scenario}
        onChange={(e) => setScenario(e.target.value)}
      />

      <button
        onClick={handleSimulate}
        className="mt-4 px-6 py-3 bg-white text-blue-600 rounded-lg font-semibold hover:bg-gray-100 transition"
      >
        Simulate Decision
      </button>

      {response && (
        <div className="mt-6 p-4 bg-white shadow rounded-lg max-w-lg text-gray-800">
          {response}
        </div>
      )}
    </div>
  );
}

export { Simulator };