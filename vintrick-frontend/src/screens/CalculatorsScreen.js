import "./CalculatorsScreen.css";
import React from "react";
import { useNavigate } from "react-router-dom";

export default function CalculatorsScreen() {
  const navigate = useNavigate();

  return (
    <div className="calculators-root">
      <div className="header-bar">
        <button className="header-back-btn" onClick={() => navigate("/")}>
          ← Back
        </button>
        <h2 className="header-title">Calculators</h2>
      </div>
      <div className="card calculators-card">
        <span className="calculators-coming">Calculators coming soon...</span>
      </div>
    </div>
  );
}
