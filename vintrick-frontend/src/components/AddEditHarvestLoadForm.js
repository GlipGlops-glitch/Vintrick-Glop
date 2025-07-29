import React, { useState, useEffect } from "react";
import { Modal, Button, Form, Spinner } from "react-bootstrap";
import PropTypes from "prop-types";
import { useSettings } from "../context/SettingsContext";
import HarvestLoadFormBody from "./HarvestLoadFormBody";

const defaultForm = {
  Vintrace_ST: null,
  Block: null,
  Tons: null,
  Press: null,
  Tank: null,
  WO: null,
  Date_Received: null,
  AgCode_ST: null,
  Time_Received: null,
  Wine_Type: null,
  Est_Tons_1: null,
  Est_Tons_2: null,
  Est_Tons_3: null,
  Press_Pick_2: null,
  Linked: null,
  Crush_Pad: null,
  Status: null,
  last_modified: null,
  synced: null,
};

export default function AddEditHarvestLoadForm({
  show,
  onClose,
  onSubmit,
  initialData,
  mode,
}) {
  const { settings } = useSettings();
  const visible = settings.harvestLoadForm.fields;

  const [form, setForm] = useState(defaultForm);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (initialData && mode === "edit") {
      setForm(initialData);
    } else {
      setForm(defaultForm);
    }
  }, [show, initialData, mode]);

  function handleChange(e) {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      // Validation removed to allow all fields to be optional
      await onSubmit(form);
      onClose(); // Close modal on success
    } catch (err) {
      setError(err.message || "Failed to submit");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Modal show={show} onHide={onClose}>
      <Form onSubmit={handleSubmit}>
        <Modal.Header closeButton>
          <Modal.Title>
            {mode === "add" ? "Add Harvest Load" : "Edit Harvest Load"}
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <HarvestLoadFormBody
            form={form}
            visible={visible}
            handleChange={handleChange}
            mode={mode}
            error={error}
            disableAll={false}
          />
          {error && <div className="text-danger mt-2">{error}</div>}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={onClose} disabled={loading}>
            Cancel
          </Button>
          <Button type="submit" variant="primary" disabled={loading}>
            {loading ? <Spinner size="sm" /> : mode === "add" ? "Add" : "Save"}
          </Button>
        </Modal.Footer>
      </Form>
    </Modal>
  );
}

AddEditHarvestLoadForm.propTypes = {
  show: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
  onSubmit: PropTypes.func.isRequired,
  initialData: PropTypes.object,
  mode: PropTypes.oneOf(["add", "edit"]).isRequired,
};
