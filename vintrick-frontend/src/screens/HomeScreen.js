// File: src/HomeScreen.js

import "./HomeScreen.css";
import React from "react";
import { useNavigate } from "react-router-dom";
import {
  GiGrapes,
  GiBarrel,
  GiCalculator,
  GiArchiveRegister,
  GiDatabase,
} from "react-icons/gi";
import vintrickLogo from "../assets/background.png"; // Import your logo

// Button grid config with icons
const navButtons = [
  { label: "Harvest", route: "/harvest-loads", icon: <GiGrapes /> },
  { label: "Blends", route: "/blends", icon: <GiBarrel /> },
  { label: "Calculators", route: "/calculators", icon: <GiCalculator /> },
  { label: "Documents", route: "/documents", icon: <GiArchiveRegister /> },
  { label: "Data", route: "/data", icon: <GiDatabase /> },
];

export default function HomeScreen() {
  const navigate = useNavigate();

  return (
    <div className="home-root">
      <div className="center-content">
        <div className="glass-card card-logo-bg">
          <img
            className="card-bg-logo-original"
            src={vintrickLogo}
            alt="Vintrick Logo"
            draggable={false}
          />
          <div className="card-bottom-nav-grid">
            <div className="nav-row">
              {navButtons.slice(0, 3).map((btn) => (
                <RippleButton
                  key={btn.label}
                  onClick={() => navigate(btn.route)}
                  icon={btn.icon}
                  label={btn.label}
                />
              ))}
            </div>
            <div className="nav-row">
              {navButtons.slice(3, 5).map((btn) => (
                <RippleButton
                  key={btn.label}
                  onClick={() => navigate(btn.route)}
                  icon={btn.icon}
                  label={btn.label}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// -- RippleButton Component with icon & ripple effect --
function RippleButton({ icon, label, onClick }) {
  const btnRef = React.useRef(null);

  function handleClick(e) {
    const btn = btnRef.current;
    const circle = document.createElement("span");
    circle.className = "ripple";
    const rect = btn.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    circle.style.width = circle.style.height = size + "px";
    circle.style.left = e.clientX - rect.left - size / 2 + "px";
    circle.style.top = e.clientY - rect.top - size / 2 + "px";
    btn.appendChild(circle);
    setTimeout(() => circle.remove(), 530);
    if (onClick) onClick(e);
  }

  return (
    <button
      className="nav-btn nav-btn-small ripple-btn"
      ref={btnRef}
      onClick={handleClick}
    >
      <span className="btn-icon">{icon}</span>
      <span>{label}</span>
    </button>
  );
}
