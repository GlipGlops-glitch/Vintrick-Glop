from pydantic import BaseModel
from typing import Optional, List, Any

# ========== Basic/Supporting Models ==========

class Tag(BaseModel):
    id: Optional[int]
    name: Optional[str]
    sort_index: Optional[int]

class Unit(BaseModel):
    description: Optional[str]
    abbreviation: Optional[str]
    key: Optional[str]
    precision: Optional[int]

class SearchDescriptive(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]

class Searchable(BaseModel):
    id: Optional[int]
    name: Optional[str]
    summary: Optional[str]
    type: Optional[str]

class SimpleCoded(BaseModel):
    id: Optional[int]
    code: Optional[str]

class Attachment(BaseModel):
    id: Optional[int]
    name: Optional[str]
    url: Optional[str]
    type: Optional[str]
    uploaded: Optional[int]
    uploaded_by: Optional[str]

# ========== Metric and Analysis Models ==========

class RateAmount(BaseModel):
    amount: Optional[str]
    rate: Optional[str]

class RateOfChangeResponse(BaseModel):
    value: Optional[float]
    sign: Optional[str]
    abs_value: Optional[float]
    unit: Optional[str]
    description: Optional[str]

class SimpleMetric(BaseModel):
    metric_name: Optional[str]
    metric_short_code: Optional[str]
    value: Optional[str]
    unit: Optional[str]
    recorded: Optional[str]
    metric_id: Optional[int]

# ========== Product & Composition Models ==========

class ProductCompositonData(BaseModel):
    key: Optional[str]
    value: Optional[float]
    value_str: Optional[str]
    volume: Optional[str]
    unit: Optional[str]

class ProductCompositonSummary(BaseModel):
    composition_view: Optional[str]
    element_data: Optional[List[ProductCompositonData]]

class ProductVolume(BaseModel):
    value: Optional[float]
    unit: Optional[str]

class ProductLiveMetricMeasurement(BaseModel):
    value: Optional[str]
    rate_of_change: Optional[RateOfChangeResponse]
    measurement_date_text: Optional[str]
    measurement_date: Optional[int]
    result_id: Optional[int]
    can_delete: Optional[bool]

class ProductLiveMetric(BaseModel):
    id: Optional[int]
    name: Optional[str]
    unit: Optional[str]
    data_type: Optional[str]
    data_type_values: Optional[str]
    min_val: Optional[int]
    max_val: Optional[int]
    measurements: Optional[List[ProductLiveMetricMeasurement]]

class FieldValuePair(BaseModel):
    key: Optional[str]
    value: Optional[Any]
    label: Optional[str]
    type: Optional[str]
    editable: Optional[bool]

class BeverageTypeProperties(BaseModel):
    alcohol: Optional[str]
    style: Optional[str]
    variety: Optional[str]
    vintage: Optional[str]
    color: Optional[str]

class Product(BaseModel):
    id: Optional[int]
    batch_code: Optional[str]
    vessel_id: Optional[int]
    description: Optional[str]
    description_can_edit: Optional[bool]
    volume: Optional[ProductVolume]
    vessel_code: Optional[str]
    has_dip_table: Optional[bool]
    dip_table_endpoint: Optional[str]
    colour: Optional[str]
    physical_product_state: Optional[str]
    vessel_type: Optional[str]
    product_status: Optional[str]
    product_analysis_endpoint: Optional[str]
    product_composition_endpoint: Optional[str]
    product_endpoint: Optional[str]
    live_metrics: Optional[List[ProductLiveMetric]]
    field_value_pairs: Optional[List[FieldValuePair]]
    can_access_notes: Optional[bool]
    notes_count: Optional[int]
    notes_endpoint: Optional[str]
    beverage_type_properties: Optional[BeverageTypeProperties]

class ProductUpdateField(BaseModel):
    property_type: Optional[str]
    property_value: Optional[str]
    property_id: Optional[int]

class ProductUpdateData(BaseModel):
    product_id: Optional[int]
    effective_date: Optional[str]
    update_fields: Optional[List[ProductUpdateField]]

class ProductListResponse(BaseModel):
    status: Optional[str]
    products: Optional[List[Product]]

class ProductResponse(BaseModel):
    status: Optional[str]
    product: Optional[Product]

class ProductUpdateResponse(BaseModel):
    status: Optional[str]
    error_list: Optional[List[str]]
    product: Optional[Product]

# ========== Block & Assessment Models ==========

class Weight(BaseModel):
    value: Optional[float]
    unit: Optional[str]

class Grading(BaseModel):
    grade: Optional[str]
    notes: Optional[str]

class LocationDetails(BaseModel):
    address: Optional[str]
    country: Optional[str]

class FullBlockAssessment(BaseModel):
    id: Optional[int]
    block: Optional[Searchable]
    vintage: Optional[int]
    assessment_date: Optional[str]
    assessed_by: Optional[Searchable]
    producing_forecast: Optional[Weight]
    available_forecast: Optional[Weight]
    intended_use: Optional[Searchable]
    harvest_method: Optional[str]
    expected_harvest_date: Optional[int]
    earliest_harvest_date: Optional[int]
    grading: Optional[Grading]
    expected_program: Optional[Searchable]
    contract: Optional[Searchable]
    spray_report_received: Optional[int]
    spray_report_attachment: Optional[Attachment]
    capital_block: Optional[bool]
    capital_project_number: Optional[str]
    crop_inspected: Optional[int]
    comments: Optional[str]
    exception_list: Optional[List[str]]
    intended_product: Optional[Searchable]
    attachments: Optional[List[Attachment]]
    location_details: Optional[LocationDetails]

# ========== Refund & Order Models ==========

class TaxAmount(BaseModel):
    name: Optional[str]
    amount: Optional[float]
    rate_pct: Optional[int]
    inclusive: Optional[bool]

class RefundLineItem(BaseModel):
    id: Optional[int]
    item_id: Optional[int]
    item_name: Optional[str]
    unit_price: Optional[int]
    return_quantity: Optional[int]
    return_total: Optional[int]
    tax_amount: Optional[float]

class Refund(BaseModel):
    id: Optional[int]
    name: Optional[str]
    refund_date: Optional[int]
    refund_date_as_text: Optional[str]
    reference: Optional[str]
    stock_returned: Optional[bool]
    storage_area_id: Optional[str]
    storage_area_name: Optional[str]
    customer_id: Optional[int]
    customer_name: Optional[str]
    refund_status: Optional[str]
    notes: Optional[str]
    sales_order_id: Optional[int]
    sales_order_name: Optional[str]
    sub_total: Optional[float]
    total: Optional[float]
    tax_breakdown: Optional[List[TaxAmount]]
    refund_line_items: Optional[List[RefundLineItem]]
    pos_sale_reference: Optional[str]

class RefundResponse(BaseModel):
    status: Optional[str]
    message: Optional[str]
    refund: Optional[List[Refund]]

class RefundUpdateResponse(BaseModel):
    status: Optional[str]
    message: Optional[str]
    refund: Optional[Refund]

class SalesOrderItem(BaseModel):
    id: Optional[int]
    item_id: Optional[int]
    item_name: Optional[str]
    unit_price: Optional[float]
    quantity: Optional[int]
    unit_of_measure: Optional[str]
    discount_pct: Optional[str]
    adjustment: Optional[str]
    tax_amount: Optional[float]
    line_total: Optional[int]
    account_id: Optional[int]
    account_code: Optional[str]
    tax_rate_id: Optional[int]
    tax_rate_name: Optional[str]
    sku: Optional[str]
    external_reference: Optional[str]

class PriceList(BaseModel):
    country_currency_code: Optional[str]
    tax_policy: Optional[str]

class SalesOrder(BaseModel):
    id: Optional[int]
    invoice_date: Optional[str]
    invoice_date_as_text: Optional[str]
    customer_id: Optional[int]
    customer_name: Optional[str]
    send_to: Optional[Searchable]
    sales_type: Optional[str]
    sales_price_list_id: Optional[int]
    sales_price_list_name: Optional[str]
    price_details: Optional[PriceList]
    sales_order_status: Optional[str]
    sales_order_items: Optional[List[SalesOrderItem]]
    code: Optional[str]
    description: Optional[str]
    reference: Optional[str]
    order_date: Optional[int]
    order_date_as_text: Optional[str]
    winery_id: Optional[str]
    winery_name: Optional[str]
    fulfillment: Optional[str]
    fulfillment_date: Optional[str]
    fulfillment_date_as_text: Optional[str]
    sales_region_id: Optional[str]
    sales_region_code: Optional[str]
    notes: Optional[str]
    customer_pickup: Optional[bool]
    disable_accounts_sync: Optional[bool]
    sub_total: Optional[int]
    tax_breakdown: Optional[List[TaxAmount]]
    total: Optional[int]
    acct_reference: Optional[str]
    pos_sale_reference: Optional[str]
    ignore_stock_error: Optional[bool]

class SalesOrderResponse(BaseModel):
    status: Optional[str]
    message: Optional[str]
    sales_orders: Optional[List[SalesOrder]]

class SalesOrderUpdateResponse(BaseModel):
    status: Optional[str]
    message: Optional[str]
    sales_orders: Optional[SalesOrder]

# ========== Stock Models ==========

class StockForm(BaseModel):
    group: Optional[str]
    variant: Optional[str]

class StockType(BaseModel):
    id: Optional[int]
    name: Optional[str]
    code: Optional[str]
    form: Optional[StockForm]

class QuantityBreakdown(BaseModel):
    on_hand: Optional[int]
    committed: Optional[int]
    ordered: Optional[int]
    available: Optional[int]

class StockItemBasics(BaseModel):
    id: Optional[int]
    code: Optional[str]
    description: Optional[str]
    endpoint: Optional[str]

class StockDistributionItem(BaseModel):
    id: Optional[int]
    item: Optional[StockItemBasics]
    winery: Optional[SearchDescriptive]
    building: Optional[SearchDescriptive]
    storage_area: Optional[SearchDescriptive]
    bay: Optional[str]
    unit: Optional[Unit]
    quantity: Optional[QuantityBreakdown]
    tax_state: Optional[Any]  # TaxState
    virtual: Optional[bool]

class StockDistributionDetail(BaseModel):
    endpoint: Optional[str]
    distributions: Optional[List[StockDistributionItem]]

class StockFieldsDetail(BaseModel):
    endpoint: Optional[str]
    fields: Optional[List[FieldValuePair]]

class StockHistoryItem(BaseModel):
    operation_id: Optional[int]
    operator_name: Optional[str]
    quantity: Optional[int]
    balance: Optional[int]
    date: Optional[int]
    workorder: Optional[SimpleCoded]
    action_type: Optional[str]
    batch: Optional[str]
    item: Optional[StockItemBasics]
    attachments: Optional[List[Attachment]]
    can_reverse: Optional[bool]

class StockHistoryItemsDetail(BaseModel):
    endpoint: Optional[str]
    first_result: Optional[int]
    max_result: Optional[int]
    total_result_count: Optional[int]
    history_items: Optional[List[StockHistoryItem]]

class StockRawComponentItem(BaseModel):
    endpoint: Optional[str]
    id: Optional[int]
    code: Optional[str]
    description: Optional[str]
    unit: Optional[Unit]
    type: Optional[StockType]
    bom_quantity: Optional[float]
    beverage_properties: Optional[BeverageTypeProperties]

class StockRawComponentsDetail(BaseModel):
    endpoint: Optional[str]
    raw_components: Optional[StockRawComponentItem]

class StockBulkInfoDetail(BaseModel):
    endpoint: Optional[str]
    message: Optional[str]
    metrics: Optional[List[SimpleMetric]]
    composition_details: Optional[List[ProductCompositonSummary]]
    additions_summary: Optional[List[Any]]  # AdditionsSummary

class StockNote(BaseModel):
    id: Optional[int]
    date: Optional[str]
    date_text: Optional[str]
    who: Optional[str]
    subject: Optional[str]
    detail: Optional[str]
    item: Optional[Searchable]
    attachments: Optional[List[Attachment]]
    inactive: Optional[bool]

class StockNotesDetail(BaseModel):
    endpoint: Optional[str]
    max_result: Optional[int]
    first_result: Optional[int]
    total_result_count: Optional[int]
    prev_url_path: Optional[str]
    next_url_path: Optional[str]
    notes: Optional[List[StockNote]]

class StockItem(BaseModel):
    id: Optional[int]
    code: Optional[str]
    description: Optional[str]
    name: Optional[str]
    inactive: Optional[bool]
    modified: Optional[int]
    type: Optional[StockType]
    category: Optional[SearchDescriptive]
    beverage_properties: Optional[BeverageTypeProperties]
    unit: Optional[Unit]
    quantity: Optional[QuantityBreakdown]
    owner: Optional[SearchDescriptive]
    wine_product: Optional[bool]
    # lot_tracked: Optional[