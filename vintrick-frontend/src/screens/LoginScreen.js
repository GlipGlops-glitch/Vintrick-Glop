// src/screens/LoginScreen.js (or wherever your login component is)
import React from "react";

export default function LoginScreen() {
  function handleFakeLogin() {
    localStorage.setItem("token", "FAKE_TOKEN_FOR_DEV");
    localStorage.setItem(
      "user",
      JSON.stringify({ name: "Dev User", email: "dev@localhost" }),
    );
    window.location.href = "/";
  }

  return (
    <div
      style={{
        maxWidth: 400,
        margin: "60px auto",
        padding: 24,
        background: "#fff",
        borderRadius: 8,
        boxShadow: "0 4px 16px #0001",
      }}
    >
      <h2>Login (Bypassed for Dev)</h2>
      <button
        onClick={handleFakeLogin}
        style={{
          width: "100%",
          padding: "12px 0",
          fontSize: 18,
          marginTop: 20,
          background: "#2176ff",
          color: "#fff",
          border: "none",
          borderRadius: 4,
        }}
      >
        Enter App (Bypass Login)
      </button>
      <p style={{ color: "gray", marginTop: 20 }}>
        Auth is bypassed for now. Remove this before production!
      </p>
    </div>
  );
}
