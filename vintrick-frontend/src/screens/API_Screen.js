// API_Screen.js

import "./API_Screen.css";
import React, { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext"; // <-- import AuthContext

export default function VintraceApiScreen() {
  const [endpointMap, setEndpointMap] = useState({});
  const [selectedEndpoint, setSelectedEndpoint] = useState("");
  const [paramValues, setParamValues] = useState({});
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const { authFetch } = useAuth(); // <-- get authFetch

  useEffect(() => {
    fetch("/endpoint_map.json")
      .then((res) => res.json())
      .then((data) => {
        const endpoints = data.endpoints || data;
        setEndpointMap(endpoints);
        const keys = Object.keys(endpoints);
        if (keys.length > 0) setSelectedEndpoint(keys[0]);
      });
  }, []);

  const handleParamChange = (param, value) => {
    setParamValues((prev) => ({ ...prev, [param]: value }));
  };

  const handleEndpointChange = (e) => {
    setSelectedEndpoint(e.target.value);
    setParamValues({});
    setOutput("");
  };

  const callApi = async () => {
    setLoading(true);
    setOutput("");
    try {
      const params = {};
      const paramList = endpointMap[selectedEndpoint]?.parameters || [];
      paramList.forEach((p) => {
        if (paramValues[p.name]) params[p.name] = paramValues[p.name];
      });
      // Use authFetch instead of fetch!
      const res = await authFetch("/api/proxy-endpoint", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ endpoint: selectedEndpoint, params }),
      });
      const result = await res.json();
      setOutput(JSON.stringify(result, null, 2));
    } catch (err) {
      setOutput(`Error: ${err}`);
    }
    setLoading(false);
  };

  const paramsUI = (endpointMap[selectedEndpoint]?.parameters || []).map(
    (param) => (
      <div className="api-param-row" key={param.name}>
        <label>
          {param.name}:&nbsp;
          <input
            type="text"
            value={paramValues[param.name] || ""}
            onChange={(e) => handleParamChange(param.name, e.target.value)}
            className="api-param-input"
          />
        </label>
      </div>
    ),
  );

  return (
    <div className="api_screen-container">
      <div className="card api-card">
        <h2 className="api-title">Vintrace API Explorer</h2>
        <div className="api-form-row">
          <label>
            <span className="api-label">Select Endpoint:&nbsp;</span>
            <select
              value={selectedEndpoint}
              onChange={handleEndpointChange}
              className="api-select"
            >
              {Object.keys(endpointMap).map((ep) => (
                <option value={ep} key={ep}>
                  {ep}
                </option>
              ))}
            </select>
          </label>
        </div>
        <div className="api-form-row">
          <strong>Parameters:</strong>
          {paramsUI.length > 0 ? (
            paramsUI
          ) : (
            <div className="api-no-params">(No parameters)</div>
          )}
        </div>
        <div className="button-bar-bg api-action-bar">
          <button
            className="nav-btn"
            onClick={callApi}
            disabled={loading || !selectedEndpoint}
            style={{ minWidth: 110 }}
          >
            {loading ? "Calling..." : "Call API"}
          </button>
        </div>
        <pre className="api-output">{output}</pre>
      </div>
    </div>
  );
}
