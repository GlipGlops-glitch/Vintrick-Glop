// src/screens/CalculatorsScreen.js

import "../styles/AppShared.css";
import React from "react";
import ModernHeaderBar from "../components/ModernHeaderBar"; // Import the new header bar
import { useNavigate } from "react-router-dom";

export default function CalculatorsScreen() {
  const navigate = useNavigate();

  return (
    <div className="calculators-root">
      <ModernHeaderBar />
      <div className="card calculators-card">
        <span className="calculators-coming">Calculators coming soon...</span>
      </div>
    </div>
  );
}