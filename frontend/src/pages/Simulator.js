import React, { useState } from "react";

function Simulator() {
  const [scenario, setScenario] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSimulate = async () => {
    if (!scenario.trim()) return;
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/simulate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ scenario }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error:", error);
      setResult({ decision: "Error connecting to backend" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-indigo-600 to-purple-600 text-white p-6">
      <h1 className="text-4xl font-bold mb-6">Ethical Decision Simulator</h1>

      <textarea
        className="w-full max-w-lg p-3 rounded-lg text-black mb-4"
        rows="5"
        placeholder="Enter your ethical scenario here..."
        value={scenario}
        onChange={(e) => setScenario(e.target.value)}
      />

      <button
        onClick={handleSimulate}
        className="px-6 py-3 bg-yellow-400 text-black font-bold rounded-lg shadow-lg hover:bg-yellow-300 transition"
        disabled={loading}
      >
        {loading ? "Simulating..." : "Run Simulation"}
      </button>

      {result && (
        <div className="mt-6 p-4 bg-white text-black rounded-lg shadow-lg max-w-lg w-full">
          <h2 className="text-xl font-semibold mb-2">Simulation Result:</h2>
          <p><strong>Scenario:</strong> {result.scenario}</p>
          <p><strong>Decision:</strong> {result.decision}</p>
        </div>
      )}
    </div>
  );
}

export default Simulator;
