import React, { useState } from "react";

export default function Simulator() {
  const [scenario, setScenario] = useState("");
  const [response, setResponse] = useState("");

  const handleSimulate = async () => {
    // later this will call the backend API
    if (!scenario.trim()) {
      setResponse("⚠️ Please enter a scenario first.");
      return;
    }

    // Temporary placeholder until backend connects
    setResponse("🤖 AI Decision: Based on ethical principles, I recommend...");
  };

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-r from-blue-500 to-purple-600 text-white">
      <div className="flex-1 flex items-center justify-center px-6">
        <div className="bg-white text-gray-900 p-8 rounded-lg shadow-lg max-w-xl w-full">
          <h2 className="text-2xl font-bold mb-4 text-center text-blue-600">
            Ethical Decision Simulator
          </h2>
          <textarea
            value={scenario}
            onChange={(e) => setScenario(e.target.value)}
            placeholder="Enter a moral dilemma or scenario..."
            className="w-full h-32 p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 mb-4"
          />
          <button
            onClick={handleSimulate}
            className="w-full px-6 py-3 bg-blue-600 text-white rounded-md font-semibold hover:bg-blue-700 transition"
          >
            Simulate Decision
          </button>

          {response && (
            <div className="mt-6 p-4 border-t text-gray-800 bg-gray-50 rounded">
              <p>{response}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
export { Simulator };