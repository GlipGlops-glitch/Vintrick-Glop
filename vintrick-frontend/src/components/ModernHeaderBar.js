// File path: vintrick-frontend/src/components/ModernHeaderBar.js

import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./ModernHeaderBar.css";
import {
  GiGrapes,
  GiBarrel,
  GiCalculator,
  GiArchiveRegister,
  GiDatabase,
} from "react-icons/gi";
import { FaRegSun, FaRegMoon, FaSearch, FaCog } from "react-icons/fa";

const navButtons = [
  { label: "Harvest", route: "/harvest-loads", icon: <GiGrapes /> },
  { label: "Blends", route: "/blends", icon: <GiBarrel /> },
  { label: "Calculators", route: "/calculators", icon: <GiCalculator /> },
  { label: "Documents", route: "/documents", icon: <GiArchiveRegister /> },
  { label: "Data", route: "/data", icon: <GiDatabase /> },
];

export default function ModernHeaderBar() {
  // Read initial theme from body for SSR/refresh support
  const [dark, setDark] = useState(() => {
    if (typeof window !== "undefined") {
      return document.body.getAttribute("data-theme") === "dark";
    }
    return false;
  });

  const navigate = useNavigate();

  // Side effect: update the global theme on body
  useEffect(() => {
    if (dark) {
      document.body.setAttribute("data-theme", "dark");
    } else {
      document.body.removeAttribute("data-theme");
    }
  }, [dark]);

  return (
    <nav className={`modern-header-bar ${dark ? "dark" : "light"}`}>
      <div className="mhb-left">
        <span className="mhb-logo-icon" style={{ fontSize: 24 }}>
          <GiGrapes />
        </span>
        <span className="mhb-logo-text">Vintrick</span>
      </div>
      <ul className="mhb-nav">
        {navButtons.map((btn) => (
          <li key={btn.route}>
            <button
              className="mhb-nav-btn"
              onClick={() => navigate(btn.route)}
              title={btn.label}
              tabIndex={0}
            >
              <span className="mhb-nav-icon">{btn.icon}</span>
              <span className="mhb-nav-label">{btn.label}</span>
            </button>
          </li>
        ))}
      </ul>
      <div className="mhb-right">
        <div className="mhb-search-bar">
          <input type="text" placeholder="Search" />
          <button>
            <FaSearch />
          </button>
        </div>
        <button
          className="mhb-theme-btn"
          onClick={() => setDark((d) => !d)}
          title={dark ? "Switch to light mode" : "Switch to dark mode"}
        >
          {dark ? <FaRegSun /> : <FaRegMoon />}
        </button>
        <button
          className="mhb-settings-btn"
          onClick={() => navigate("/settings")}
          title="Settings"
        >
          <FaCog />
        </button>
      </div>
    </nav>
  );
}