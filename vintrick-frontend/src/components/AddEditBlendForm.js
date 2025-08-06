// src/components/AddEditBlendForm.js

import React, { useState, useEffect } from "react";
import { Modal, Button, Form } from "react-bootstrap";
import BlendFormBody from "./BlendFormBody";

const FIELDS = [
  "Title", "Brand", "Varietal", "Vintage", "WineType"
];

function getInitFormData(data = {}) {
  // Always return strings for all fields
  return FIELDS.reduce(
    (acc, field) => ({
      ...acc,
      [field]: typeof data[field] === "string" ? data[field] : (data[field] != null ? String(data[field]) : "")
    }),
    { ID: data.ID || undefined }
  );
}

export default function AddEditBlendForm({
  show,
  onClose,
  onSubmit,
  initialData = {},
  mode = "add"
}) {
  const [formData, setFormData] = useState(getInitFormData(initialData));

  // Only reset when opening the modal
  useEffect(() => {
    if (show) {
      setFormData(getInitFormData(initialData));
    }
    // Do NOT include initialData in dependencies to prevent reset on every change
    // eslint-disable-next-line
  }, [show]);

  function handleChange(e) {
    const { name, value } = e.target;
    setFormData(data => ({
      ...data,
      [name]: value
    }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit(formData);
  }

  return (
    <Modal show={show} onHide={onClose} backdrop="static" centered>
      <Form onSubmit={handleSubmit}>
        <Modal.Header closeButton>
          <Modal.Title>
            {mode === "edit" ? "Edit Blend" : "Add Blend"}
          </Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <BlendFormBody formData={formData} handleChange={handleChange} />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={onClose}>
            Cancel
          </Button>
          <Button type="submit" variant="primary">
            Save
          </Button>
        </Modal.Footer>
      </Form>
    </Modal>
  );
}