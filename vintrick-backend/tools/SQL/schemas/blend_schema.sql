-- vintrick-backend/tools/SQL/schemas/bottling_specs_schema.sql

CREATE TABLE bottling_specs (
    id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),

    Title NVARCHAR(MAX) NULL,
    Brand NVARCHAR(MAX) NULL,
    Varietal NVARCHAR(MAX) NULL,
    Vintage NVARCHAR(MAX) NULL,
    Wine_Type NVARCHAR(50) NULL,
    FG_Num NVARCHAR(MAX) NULL,
    Bulk_Num NVARCHAR(MAX) NULL,
    Spec_Sheet NVARCHAR(50) NULL,
    AVA NVARCHAR(MAX) NULL,
    Status NVARCHAR(50) NULL,
    Expected_Bottle_Date DATETIME NULL,
    Starting_RS_g_L FLOAT NULL,
    Target_RS_g_L FLOAT NULL,
    Sweetener NVARCHAR(50) NULL,
    Finishing_Cu_ppm FLOAT NULL,
    Finishing_Malic_ppm FLOAT NULL,
    Finish_PVPP_ppm FLOAT NULL,
    CO2_Tank_Min_ppm FLOAT NULL,
    CO2_Tank_Max_ppm FLOAT NULL,
    Velcorin_Needed BIT NULL,
    CO2_Bottle_Min_ppm FLOAT NULL,
    CO2_Bottle_Max_ppm FLOAT NULL,
    DIT_Rate FLOAT NULL,
    Stabivin_SP NVARCHAR(MAX) NULL,
    Surli_Velvet_Plus NVARCHAR(MAX) NULL,
    ML NVARCHAR(50) NULL,
    Screwcap NVARCHAR(50) NULL,
    Alc FLOAT NULL,
    Pre_Filter NVARCHAR(50) NULL,
    Final_Filter NVARCHAR(50) NULL,
    Tier NVARCHAR(50) NULL,
    Label_Alc NVARCHAR(MAX) NULL,
    Lot_Num NVARCHAR(MAX) NULL,
    Is_First_Bottling NVARCHAR(50) NULL,
    Has_Allergens NVARCHAR(50) NULL,
    Total_Acidity_g_100ml FLOAT NULL,
    PH FLOAT NULL,
    SO2_Target_ppm FLOAT NULL,
    Malate_ppm NVARCHAR(MAX) NULL,
    RS_Invert_g_100ml NVARCHAR(MAX) NULL,
    Bottle_DO_Range_Min_Max NVARCHAR(MAX) NULL,
    -- RS_Approval_Min_g_100ml FLOAT NULL, -- CALCULATED
    -- RS_Approval_Max_g_100ml FLOAT NULL, -- CALCULATED
    -- RS_Approval_Range_g_100ml NVARCHAR(MAX) NULL, -- CALCULATED
    -- Bottling_CO2_Range_min_max NVARCHAR(MAX) NULL, -- CALCULATED
    -- Bottling_SO2_ppm_min_max NVARCHAR(MAX) NULL, -- CALCULATED
    -- Bottling_Alc_Range_min FLOAT NULL, -- CALCULATED
    -- Bottling_Alc_Range_max FLOAT NULL, -- CALCULATED
    -- Bottling_Alcohol_Range_min_max NVARCHAR(MAX) NULL, -- CALCULATED
    Malic_ppm FLOAT NULL,
    PVPP_ppm FLOAT NULL,
    Lactic_ppm FLOAT NULL,
    Arabinol_gal_1000gal FLOAT NULL,
    KWK_Rate_num_1000gal FLOAT NULL,
    CofT_Rate_num_1000 FLOAT NULL,
    HeatStable BIT NULL,
    Need_STARS BIT NULL,
    Cu_ppm FLOAT NULL,
    -- RS_Approval_Min_g_L FLOAT NULL, -- CALCULATED
    -- RS_Approval_Max_g_L FLOAT NULL, -- CALCULATED
    -- SO2_Min_ppm FLOAT NULL, -- CALCULATED
    -- SO2_Max_ppm FLOAT NULL, -- CALCULATED
    -- RS_Approval_Range_g_L NVARCHAR(MAX) NULL, -- CALCULATED
    Extract_g_L FLOAT NULL,
    -- Extract_Min_g_L FLOAT NULL, -- CALCULATED
    -- Extract_Max_g_L FLOAT NULL, -- CALCULATED
    -- Extract_Range_g_L NVARCHAR(MAX) NULL, -- CALCULATED
    Bottling_SO2_ppm_min_max_Override NVARCHAR(MAX) NULL,
    Extract_Range_g_L_Override NVARCHAR(MAX) NULL,
    RS_Approval_Range_g_L_Override NVARCHAR(MAX) NULL,
    Step_1 NVARCHAR(MAX) NULL,
    Step_2 NVARCHAR(MAX) NULL,
    Step_3 NVARCHAR(MAX) NULL,
    Step_4 NVARCHAR(MAX) NULL,
    Step_5 NVARCHAR(MAX) NULL,
    Step_6 NVARCHAR(MAX) NULL,
    Step_1_Comments NVARCHAR(MAX) NULL,
    Step_2_Comments NVARCHAR(MAX) NULL,
    Step_3_Comments NVARCHAR(MAX) NULL,
    Test_Label NVARCHAR(MAX) NULL,
    Vintage_Roll NVARCHAR(MAX) NULL,
    Finishing_Cu_Toggle NVARCHAR(MAX) NULL,
    Allergens NVARCHAR(MAX) NULL,
    Bottling_SO2_ppm_min_Override FLOAT NULL,
    Bottling_SO2_ppm_max_Override FLOAT NULL,
    RS_Approval_Range_g_L_Min_Override FLOAT NULL,
    RS_Approval_Range_g_L_Max_Override FLOAT NULL,
    Extract_g_L_Min_Override FLOAT NULL,
    Extract_g_L_Max_Override FLOAT NULL,
    Label_1 NVARCHAR(MAX) NULL,
    CO2_Override NVARCHAR(MAX) NULL,
    -- Vegan NVARCHAR(MAX) NULL, -- CALCULATED
    CO2_Tanker_Min_ppm FLOAT NULL,
    CO2_Tanker_Max_ppm FLOAT NULL,
    Malate_g_L NVARCHAR(MAX) NULL,
    Tech_Sheet_Needed NVARCHAR(MAX) NULL,
    Wine_Library_Order_Needed NVARCHAR(MAX) NULL,
    Label_Verification_Needed NVARCHAR(MAX) NULL,
    Finishing_Cu NVARCHAR(50) NULL,
    First_Bottling_Run NVARCHAR(50) NULL,
    FG_sub_1 NVARCHAR(MAX) NULL,
    FG_sub_2 NVARCHAR(MAX) NULL,
    Date_Notified NVARCHAR(MAX) NULL,
    Notified_By NVARCHAR(MAX) NULL,

    Modified DATETIME NULL,
    Created DATETIME NULL,
    Created_By NVARCHAR(100) NULL,
    Modified_By NVARCHAR(100) NULL
);