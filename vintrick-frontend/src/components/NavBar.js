// src/components/NavBar.js
import React from "react";
import { useNavigate, useLocation } from "react-router-dom";

const navItems = [
  { label: "Harvest", path: "/harvest" },
  { label: "Blends", path: "/blends" },
  { label: "Calculators", path: "/calculators" },
  { label: "Documents", path: "/documents" },
  { label: "Data", path: "/data" },
];

export default function NavBar() {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <nav
      style={{
        display: "flex",
        justifyContent: "space-around",
        background: "#222",
        padding: "12px 0",
        position: "fixed",
        bottom: 0,
        left: 0,
        width: "100%",
        zIndex: 10,
      }}
    >
      {navItems.map(({ label, path }) => (
        <button
          key={label}
          style={{
            fontWeight: "bold",
            padding: "10px 30px",
            borderRadius: 8,
            border: location.pathname === path ? "2px solid #fff" : "none",
            background: location.pathname === path ? "#007bff" : "#444",
            color: "#fff",
            fontSize: 18,
            cursor: "pointer",
          }}
          onClick={() => navigate(path)}
        >
          {label}
        </button>
      ))}
    </nav>
  );
}
