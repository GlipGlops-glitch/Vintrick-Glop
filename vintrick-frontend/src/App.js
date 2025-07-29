// src/App.js

import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
} from "react-router-dom";

// Import screens
import HomeScreen from "./screens/HomeScreen";
import BlendsScreen from "./screens/BlendsScreen";
import BlendDetailScreen from "./screens/BlendDetailScreen";
import CalculatorsScreen from "./screens/CalculatorsScreen";
import DataScreen from "./screens/DataScreen";
import DetailsScreen from "./screens/DetailsScreen";
import DocumentsScreen from "./screens/DocumentsScreen";
import HarvestLoadsScreen from "./screens/HarvestLoadsScreen";
import API_Screen from "./screens/API_Screen";
import SettingsScreen from "./screens/SettingsScreen";
import HarvestLoadFormSettings from "./screens/HarvestLoadFormSettings";

// Auth
import LoginScreen from "./screens/LoginScreen";
import ProtectedRoute from "./components/ProtectedRoute";
import { AuthProvider } from "./context/AuthContext";
import { SettingsProvider } from "./context/SettingsContext";

// Styles
import "bootstrap/dist/css/bootstrap.min.css";
import "./screens/HomeScreen.css";

// Shared button style for both buttons
const btnStyle = {
  width: 150,
  height: 48,
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  borderRadius: 16,
  border: 0,
  fontWeight: 700,
  fontFamily: "inherit",
  fontSize: "1.08rem",
  boxShadow: "0 2px 14px rgba(80,70,140,0.14)",
  cursor: "pointer",
  position: "fixed",
  right: 24,
  zIndex: 999,
  transition: "background 0.2s, color 0.2s",
};

function ThemeToggle() {
  const [isDark, setIsDark] = React.useState(
    () => document.body.getAttribute("data-theme") === "dark",
  );

  React.useEffect(() => {
    const saved = localStorage.getItem("theme");
    if (saved) {
      document.body.setAttribute("data-theme", saved);
      setIsDark(saved === "dark");
    } else {
      const prefersDark =
        window.matchMedia &&
        window.matchMedia("(prefers-color-scheme: dark)").matches;
      if (prefersDark) {
        document.body.setAttribute("data-theme", "dark");
        setIsDark(true);
      }
    }
  }, []);

  function toggleTheme() {
    const isCurrentlyDark = document.body.getAttribute("data-theme") === "dark";
    if (isCurrentlyDark) {
      document.body.removeAttribute("data-theme");
      localStorage.setItem("theme", "light");
      setIsDark(false);
    } else {
      document.body.setAttribute("data-theme", "dark");
      localStorage.setItem("theme", "dark");
      setIsDark(true);
    }
  }
  return (
    <button
      aria-label="Toggle dark mode"
      onClick={toggleTheme}
      style={{
        ...btnStyle,
        top: 24,
        background: "linear-gradient(90deg, #8e9eab 0%, #636fa4 100%)",
        color: "#fff",
        gap: 8,
      }}
    >
      <span style={{ fontSize: 22 }}>{isDark ? "☀️" : "🌙"}</span>
      <span style={{ fontWeight: 700 }}>{isDark ? "Light" : "Dark"}</span>
    </button>
  );
}

function SettingsButton() {
  const navigate = useNavigate();
  return (
    <button
      aria-label="Go to settings"
      onClick={() => navigate("/settings")}
      style={{
        ...btnStyle,
        top: 84,
        background: "linear-gradient(90deg, #54577a 0%, #363a54 100%)",
        color: "#fff",
        gap: 8,
      }}
    >
      <span style={{ fontSize: 22 }}>⚙️</span>
      <span style={{ fontWeight: 700 }}>Settings</span>
    </button>
  );
}

function AppRoutes() {
  return (
    <>
      <ThemeToggle />
      <SettingsButton />
      <Routes>
        <Route path="/login" element={<LoginScreen />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <HomeScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/blends"
          element={
            <ProtectedRoute>
              <BlendsScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/blend-details"
          element={
            <ProtectedRoute>
              <BlendDetailScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/calculators"
          element={
            <ProtectedRoute>
              <CalculatorsScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/data"
          element={
            <ProtectedRoute>
              <DataScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/details"
          element={
            <ProtectedRoute>
              <DetailsScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/documents"
          element={
            <ProtectedRoute>
              <DocumentsScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/harvest-loads"
          element={
            <ProtectedRoute>
              <HarvestLoadsScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/api"
          element={
            <ProtectedRoute>
              <API_Screen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/harvest"
          element={
            <ProtectedRoute>
              <HarvestLoadsScreen />
            </ProtectedRoute>
          }
        />

        {/* Settings screens */}
        <Route
          path="/settings"
          element={
            <ProtectedRoute>
              <SettingsScreen />
            </ProtectedRoute>
          }
        />
        <Route
          path="/settings/harvestload-form"
          element={
            <ProtectedRoute>
              <HarvestLoadFormSettings />
            </ProtectedRoute>
          }
        />

        {/* 404 fallback */}
        <Route
          path="*"
          element={
            <ProtectedRoute>
              <HomeScreen />
            </ProtectedRoute>
          }
        />
      </Routes>
    </>
  );
}

function App() {
  return (
    <AuthProvider>
      <SettingsProvider>
        <Router>
          <AppRoutes />
        </Router>
      </SettingsProvider>
    </AuthProvider>
  );
}

export default App;
