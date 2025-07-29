// src/components/HeaderBar.js

import React from "react";
import { Button } from "react-bootstrap";
import "./HeaderBar.css";
import { useAuth } from "../context/AuthContext";

export default function HeaderBar({
  title,
  onBack,
  onAdd,
  addLabel = "+ Add",
}) {
  const { user, logout } = useAuth();

  return (
    <div className="header-bar">
      {onBack ? (
        <Button
          variant="outline-secondary"
          className="header-back-btn"
          onClick={onBack}
        >
          ← Back
        </Button>
      ) : (
        <div style={{ width: 94 }} /> // Spacer for symmetry
      )}
      <h2 className="header-title">{title}</h2>
      <div
        style={{
          width: 200,
          display: "flex",
          alignItems: "center",
          justifyContent: "flex-end",
        }}
      >
        {user && (
          <>
            <span style={{ marginRight: 8 }}>{user.name || user.email}</span>
            <Button variant="outline-danger" size="sm" onClick={logout}>
              Logout
            </Button>
          </>
        )}
        {!user && <div style={{ width: 94 }} />}
        {onAdd && (
          <Button variant="primary" className="header-add-btn" onClick={onAdd}>
            {addLabel}
          </Button>
        )}
      </div>
    </div>
  );
}
