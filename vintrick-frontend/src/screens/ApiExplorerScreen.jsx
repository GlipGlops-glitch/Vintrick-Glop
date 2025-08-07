// src/screens/ApiExplorerScreen.jsx

import React from "react";
import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";

// Point this to your FastAPI backend's OpenAPI spec URL
const API_SPEC_URL = "http://localhost:3000/openapi.json";

const ApiExplorerScreen = () => {
  return (
    <div style={{ height: "100vh" }}>
      <SwaggerUI url={API_SPEC_URL} docExpansion="list" />
    </div>
  );
};

export default ApiExplorerScreen;