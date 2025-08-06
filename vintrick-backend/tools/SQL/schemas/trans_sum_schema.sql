-- vintrick-backend/tools/SQL/schemas/trans_sum_schema.sql

-- VesselDetails table
IF OBJECT_ID('vessel_details', 'U') IS NULL
CREATE TABLE vessel_details (
    id INT IDENTITY PRIMARY KEY,
    contentsId INT NULL,
    batch NVARCHAR(255) NULL,
    batchId INT NULL,
    volume INT NULL,
    volumeUnit NVARCHAR(32) NULL,
    dip NVARCHAR(32) NULL,
    state NVARCHAR(64) NULL,
    rawTaxClass NVARCHAR(128) NULL,
    federalTaxClass NVARCHAR(128) NULL,
    stateTaxClass NVARCHAR(128) NULL,
    program NVARCHAR(128) NULL
);

-- Vessel table
IF OBJECT_ID('vessels', 'U') IS NULL
CREATE TABLE vessels (
    id INT IDENTITY PRIMARY KEY,
    name NVARCHAR(255) NULL,
    vessel_id INT NULL,
    before_details_id INT NULL REFERENCES vessel_details(id),
    after_details_id INT NULL REFERENCES vessel_details(id),
    volOut INT NULL,
    volOutUnit NVARCHAR(32) NULL,
    volIn INT NULL,
    volInUnit NVARCHAR(32) NULL
);

-- LossDetails table
IF OBJECT_ID('loss_details', 'U') IS NULL
CREATE TABLE loss_details (
    id INT IDENTITY PRIMARY KEY,
    volume INT NULL,
    volumeUnit NVARCHAR(32) NULL,
    reason NVARCHAR(255) NULL
);

-- Additives table
IF OBJECT_ID('additives', 'U') IS NULL
CREATE TABLE additives (
    id INT IDENTITY PRIMARY KEY,
    additive_id INT NULL,
    name NVARCHAR(255) NULL,
    description NVARCHAR(255) NULL
);

-- AdditionOps table
IF OBJECT_ID('addition_ops', 'U') IS NULL
CREATE TABLE addition_ops (
    id INT IDENTITY PRIMARY KEY,
    vesselId INT NULL,
    vesselName NVARCHAR(255) NULL,
    batchId INT NULL,
    batchName NVARCHAR(255) NULL,
    templateId INT NULL,
    templateName NVARCHAR(255) NULL,
    changeToState NVARCHAR(255) NULL,
    volume NVARCHAR(64) NULL,
    amount FLOAT NULL,
    unit NVARCHAR(32) NULL,
    lotNumbers NVARCHAR(MAX) NULL,
    additive_id INT NULL REFERENCES additives(id)
);

-- AnalysisOps table
IF OBJECT_ID('analysis_ops', 'U') IS NULL
CREATE TABLE analysis_ops (
    id INT IDENTITY PRIMARY KEY,
    vesselId INT NULL,
    vesselName NVARCHAR(255) NULL,
    batchId INT NULL,
    batchName NVARCHAR(255) NULL,
    templateId INT NULL,
    templateName NVARCHAR(255) NULL
);

-- MetricAnalysis table
IF OBJECT_ID('metric_analysis', 'U') IS NULL
CREATE TABLE metric_analysis (
    id INT IDENTITY PRIMARY KEY,
    name NVARCHAR(255) NULL,
    value FLOAT NULL,
    txtValue NVARCHAR(255) NULL,
    unit NVARCHAR(32) NULL,
    analysis_ops_id INT NULL REFERENCES analysis_ops(id)
);

-- TransSum (transaction summary) table
IF OBJECT_ID('trans_sums', 'U') IS NULL
CREATE TABLE trans_sums (
    id INT IDENTITY PRIMARY KEY,
    formattedDate NVARCHAR(32) NULL,
    date BIGINT NULL,
    operationId INT NULL,
    operationTypeId INT NULL,
    operationTypeName NVARCHAR(128) NULL,
    subOperationTypeId INT NULL,
    subOperationTypeName NVARCHAR(128) NULL,
    workorder NVARCHAR(128) NULL,
    jobNumber NVARCHAR(128) NULL,
    treatment NVARCHAR(128) NULL,
    assignedBy NVARCHAR(128) NULL,
    completedBy NVARCHAR(128) NULL,
    winery NVARCHAR(128) NULL,
    from_vessel_id INT NULL REFERENCES vessels(id),
    to_vessel_id INT NULL REFERENCES vessels(id),
    loss_details_id INT NULL REFERENCES loss_details(id),
    addition_ops_id INT NULL REFERENCES addition_ops(id),
    analysis_ops_id INT NULL REFERENCES analysis_ops(id),
    additionalDetails NVARCHAR(MAX) NULL
);