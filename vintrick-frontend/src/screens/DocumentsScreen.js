// DocumentsScreen.js

import "./DocumentsScreen.css";
import React from "react";
import HeaderBar from "../components/HeaderBar";
import { useNavigate } from "react-router-dom";

export default function DocumentsScreen() {
  const navigate = useNavigate();
  return (
    <div className="documents-root">
      <HeaderBar title="Documents" onBack={() => navigate(-1)} />
      <div className="card documents-card">
        <span className="documents-coming">Documents coming soon...</span>
      </div>
    </div>
  );
}
