CREATE TABLE shipments (
    uid UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    id INT NULL, -- system shipment id
    work_order_number NVARCHAR(50) NULL,
    job_number NVARCHAR(50) NULL,
    shipment_number NVARCHAR(50) NULL,
    type NVARCHAR(50) NULL,

    -- Source object
    source_id INT NULL,
    source_name NVARCHAR(100) NULL,
    source_business_unit NVARCHAR(100) NULL,

    -- Destination object - Winery
    destination_winery_id INT NULL,
    destination_winery_name NVARCHAR(100) NULL,
    destination_winery_business_unit NVARCHAR(100) NULL,

    -- Destination object - Party
    destination_party_id INT NULL,
    destination_party_name NVARCHAR(100) NULL,
    destination_party_extId NVARCHAR(100) NULL,

    occurred_time BIGINT NULL,
    modified_time BIGINT NULL,

    -- Carrier
    carrier_id INT NULL,
    carrier_name NVARCHAR(100) NULL,
    carrier_extId NVARCHAR(100) NULL,

    reference NVARCHAR(100) NULL,

    -- Dispatch Type
    dispatch_type_id INT NULL,
    dispatch_type_name NVARCHAR(100) NULL,

    -- Freight Code
    freight_code_id INT NULL,
    freight_code_name NVARCHAR(50) NULL,

    reversed BIT DEFAULT 0 NULL,
    last_modified DATETIME NULL,
    synced BIT DEFAULT 0 NULL,

    -- Optionally store full JSON for wineDetails, allocations, metrics
    wine_details NVARCHAR(MAX) NULL,
    wine_allocations NVARCHAR(MAX) NULL,
    wine_metrics NVARCHAR(MAX) NULL
);