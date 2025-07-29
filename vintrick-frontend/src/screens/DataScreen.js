import "./DataScreen.css";
import React, { useState } from "react";
import HeaderBar from "../components/HeaderBar";
import { useNavigate } from "react-router-dom";

const ALL_COLUMNS = [
  "Task",
  "Scheduled",
  "Crush Pad",
  "Time",
  "Comment",
  "Ranch",
  "Block",
  "Allocation",
  "Tons",
  "Brand",
  "Ferm Site",
  "Variety",
  "Pick",
  "Analysis",
  "Date",
  "Brix",
  "pH",
  "TA",
];

export default function DataScreen() {
  const [testMode, setTestMode] = useState(true);
  const [preview, setPreview] = useState({
    open: false,
    title: "",
    content: "",
  });
  const [fieldMappingOpen, setFieldMappingOpen] = useState(false);
  const navigate = useNavigate();

  // --- Button Handlers ---
  const handlePreviewBookings = () =>
    setPreview({
      open: true,
      title: "Bookings Preview",
      content: "File preview not implemented yet.",
    });
  const handleImportBookings = () =>
    alert("Import/Post Bookings not implemented yet.");
  const handlePreviewFruit = () =>
    setPreview({
      open: true,
      title: "Fruit Intake Preview",
      content: "Fruit intake preview not implemented yet.",
    });
  const handleImportFruit = () =>
    alert("Import/Post Fruit Intake not implemented yet.");
  const handleViewAllBookings = () =>
    alert("View All Bookings not implemented yet.");
  const handleViewAllFruit = () =>
    alert("View All Fruit Intake not implemented yet.");
  const handleFieldMapping = () => setFieldMappingOpen(true);

  return (
    <div className="datascreen-root">
      <div className="card datascreen-card">
        <HeaderBar
          title="Data Import, Bookings, & Fruit Intake API"
          onBack={() => navigate(-1)}
        />
        <div className="datascreen-btn-group">
          <button
            className="nav-btn datascreen-btn"
            onClick={handlePreviewBookings}
          >
            Preview Bookings Upload
          </button>
          <button
            className="nav-btn datascreen-btn nav-btn-blue"
            onClick={handleImportBookings}
          >
            Import/Post Bookings
          </button>
          <button
            className="nav-btn datascreen-btn"
            onClick={handlePreviewFruit}
          >
            Preview Fruit Intake Upload
          </button>
          <button
            className="nav-btn datascreen-btn nav-btn-green"
            onClick={handleImportFruit}
          >
            Import/Post Fruit Intake
          </button>
          <button
            className="nav-btn datascreen-btn"
            onClick={handleViewAllBookings}
          >
            View All Bookings
          </button>
          <button
            className="nav-btn datascreen-btn"
            onClick={handleViewAllFruit}
          >
            View All Fruit Intake
          </button>
          <button
            className="nav-btn datascreen-btn nav-btn-light"
            onClick={handleFieldMapping}
          >
            Field Mapping
          </button>
        </div>
        <div className="datascreen-testmode">
          <label htmlFor="testModeToggle">Test</label>
          <input
            id="testModeToggle"
            type="checkbox"
            checked={testMode}
            onChange={() => setTestMode(!testMode)}
          />
        </div>

        {/* Preview Modal */}
        {preview.open && (
          <Modal
            title={preview.title}
            onClose={() => setPreview({ ...preview, open: false })}
          >
            <pre className="datascreen-modal-pre">{preview.content}</pre>
          </Modal>
        )}

        {/* Field Mapping Modal (Stub) */}
        {fieldMappingOpen && (
          <Modal
            title="Field Mapping"
            onClose={() => setFieldMappingOpen(false)}
          >
            <div>
              <p>This would show a field mapping UI.</p>
              <button
                className="nav-btn"
                onClick={() => setFieldMappingOpen(false)}
              >
                Close
              </button>
            </div>
          </Modal>
        )}
      </div>
    </div>
  );
}

// --- Modal component with themed style ---
function Modal({ title, onClose, children }) {
  return (
    <div className="datascreen-modal-backdrop">
      <div className="datascreen-modal-card">
        <h3>{title}</h3>
        <div>{children}</div>
        <button
          className="nav-btn"
          style={{ marginTop: 16, float: "right" }}
          onClick={onClose}
        >
          Close
        </button>
      </div>
    </div>
  );
}
