import "./HarvestLoadsScreen.css"; // Use shared theme/css
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import HeaderBar from "../components/HeaderBar";
import axios from "axios";

const ALL_COLUMNS = [
  "Task", "Scheduled", "Crush Pad", "Time", "Comment", "Ranch", "Block", "Allocation", "Tons",
  "Brand", "Ferm Site", "Variety", "Pick", "Analysis", "Date", "Brix", "pH", "TA",
];

export default function DataScreen() {
  const [testMode, setTestMode] = useState(true);
  const [preview, setPreview] = useState({ open: false, title: "", content: "" });
  const [fieldMappingOpen, setFieldMappingOpen] = useState(false);
  const [uploadStatus, setUploadStatus] = useState("");
  const navigate = useNavigate();

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

  const handleSqlUpload = async () => {
    setUploadStatus("Uploading...");
    try {
      const res = await axios.post("/api/data/sql-upload");
      if (res.data && res.data.success) {
        setUploadStatus("✅ SQL upload complete!");
      } else {
        setUploadStatus("❌ SQL upload failed.");
      }
    } catch (err) {
      setUploadStatus("❌ Error during SQL upload.");
    }
  };

  return (
    <div className="harvestloads-root">
      <HeaderBar
        title="Data Import, Bookings, & Fruit Intake API"
        onBack={() => navigate(-1)}
      />
      <div className="card harvestloads-card">
        <div className="harvestloads-controls" style={{ flexWrap: "wrap" }}>
          <button className="nav-btn nav-btn-light" onClick={handlePreviewBookings}>
            Preview Bookings Upload
          </button>
          <button className="nav-btn nav-btn-blue" onClick={handleImportBookings}>
            Import/Post Bookings
          </button>
          <button className="nav-btn nav-btn-light" onClick={handlePreviewFruit}>
            Preview Fruit Intake Upload
          </button>
          <button className="nav-btn nav-btn-green" onClick={handleImportFruit}>
            Import/Post Fruit Intake
          </button>
          <button className="nav-btn nav-btn-light" onClick={handleViewAllBookings}>
            View All Bookings
          </button>
          <button className="nav-btn nav-btn-light" onClick={handleViewAllFruit}>
            View All Fruit Intake
          </button>
          <button className="nav-btn nav-btn-light" onClick={handleFieldMapping}>
            Field Mapping
          </button>
          <button className="nav-btn nav-btn-orange" onClick={handleSqlUpload}>
            SQL Server Upload
          </button>
        </div>
        <div className="harvestloads-controls" style={{ marginBottom: 0 }}>
          <label htmlFor="testModeToggle" style={{ marginRight: 8 }}>
            Test
          </label>
          <input
            id="testModeToggle"
            type="checkbox"
            checked={testMode}
            onChange={() => setTestMode(!testMode)}
          />
        </div>

        {uploadStatus && (
          <div className="datascreen-status">{uploadStatus}</div>
        )}

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
                className="nav-btn nav-btn-light"
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
          className="nav-btn nav-btn-light"
          style={{ marginTop: 16, float: "right" }}
          onClick={onClose}
        >
          Close
        </button>
      </div>
    </div>
  );
}