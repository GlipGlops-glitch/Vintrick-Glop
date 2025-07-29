import "./BlendDetailScreen.css";
import React from "react";
import { useNavigate } from "react-router-dom";
import HeaderBar from "../components/HeaderBar"; // If using the reusable header

function BlendDetailScreen() {
  const navigate = useNavigate();

  return (
    <div className="blenddetailscreen-root">
      <HeaderBar title="Blend Details" onBack={() => navigate("/blends")} />

      <div className="card blenddetails-card">
        <span className="blenddetails-coming">
          Blend Details coming soon...
        </span>
      </div>
    </div>
  );
}

export default BlendDetailScreen;
