// src/screens/DocumentsScreen.js

import "../styles/AppShared.css";
import React from "react";
import ModernHeaderBar from "../components/ModernHeaderBar"; // Use the new header bar
import { useNavigate } from "react-router-dom";

export default function DocumentsScreen() {
  const navigate = useNavigate();
  return (
    <div className="documents-root">
      <ModernHeaderBar />
      <div className="card documents-card">
        <span className="documents-coming">Documents coming soon...</span>
      </div>
    </div>
  );
}