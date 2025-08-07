// vintrick-frontend/src/App.js

import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
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
import ApiExplorerScreen from "./screens/ApiExplorerScreen"; // <-- Added Swagger UI screen

// Auth
import LoginScreen from "./screens/LoginScreen";
import ProtectedRoute from "./components/ProtectedRoute";
import { AuthProvider } from "./context/AuthContext";
import { SettingsProvider } from "./context/SettingsContext";

// Styles
import "bootstrap/dist/css/bootstrap.min.css";
import "./screens/HomeScreen.css";

// Import logo directly for correct path resolution
import vintrickLogo from "./assets/background.png";

function AppRoutes() {
  return (
    <>
      <Routes>
        <Route path="/login" element={<LoginScreen />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <HomeScreen logoSrc={vintrickLogo} />
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

        {/* Swagger UI Explorer Route */}
        <Route
          path="/api-explorer"
          element={
            <ProtectedRoute>
              <ApiExplorerScreen />
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
              <HomeScreen logoSrc={vintrickLogo} />
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