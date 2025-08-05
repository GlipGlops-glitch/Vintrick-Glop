# vintrick-backend/tools/extract_shipment_flat.py
# Usage: Call extract_flat_shipment(json_obj) for each shipment JSON object.
# Returns a dict with all fields flattened for SQL insert or API POST.

import json

def extract_flat_shipment(obj):
    # Top-level fields
    out = {
        "id": obj.get("id"),
        "workOrderNumber": obj.get("workOrderNumber"),
        "jobNumber": obj.get("jobNumber"),
        "shipmentNumber": obj.get("shipmentNumber"),
        "type": obj.get("type"),
        "occurredTime": obj.get("occurredTime"),
        "modifiedTime": obj.get("modifiedTime"),
        "reference": obj.get("reference"),
        "reversed": obj.get("reversed"),
    }

    # Source
    source = obj.get("source", {})
    out["source_id"] = source.get("id")
    out["source_name"] = source.get("name")
    out["source_businessUnit"] = source.get("businessUnit")

    # Destination
    destination = obj.get("destination", {})
    winery = destination.get("winery", {})
    party = destination.get("party", {})
    out["destination_winery_id"] = winery.get("id")
    out["destination_winery_name"] = winery.get("name")
    out["destination_winery_businessUnit"] = winery.get("businessUnit")
    out["destination_party_id"] = party.get("id")
    out["destination_party_name"] = party.get("name")
    out["destination_party_extId"] = party.get("extId")

    # Carrier
    carrier = obj.get("carrier", {})
    out["carrier_id"] = carrier.get("id")
    out["carrier_name"] = carrier.get("name")
    out["carrier_extId"] = carrier.get("extId")

    # DispatchType
    dispatch_type = obj.get("dispatchType", {})
    out["dispatchType_id"] = dispatch_type.get("id")
    out["dispatchType_name"] = dispatch_type.get("name")

    # FreightCode
    freight_code = obj.get("freightCode", {})
    out["freightCode_id"] = freight_code.get("id")
    out["freightCode_name"] = freight_code.get("name")

    # WineDetails (array, flatten as JSON string)
    wine_details = obj.get("wineDetails", [])
    out["wineDetails"] = json.dumps(wine_details)

    # Optionally, extract and flatten the first wine detail (if you want individual columns)
    if wine_details:
        wd = wine_details[0]
        out["wine_vessel"] = wd.get("vessel")
        out["wine_batch"] = wd.get("batch")
        # WineBatch
        wine_batch = wd.get("wineBatch", {})
        out["wineBatch_id"] = wine_batch.get("id")
        out["wineBatch_name"] = wine_batch.get("name")
        out["wineBatch_description"] = wine_batch.get("description")
        out["wineBatch_vintage"] = wine_batch.get("vintage")
        designated_region = wine_batch.get("designatedRegion", {})
        out["wineBatch_designatedRegion_id"] = designated_region.get("id")
        out["wineBatch_designatedRegion_name"] = designated_region.get("name")
        out["wineBatch_designatedRegion_code"] = designated_region.get("code")
        designated_variety = wine_batch.get("designatedVariety", {})
        out["wineBatch_designatedVariety_id"] = designated_variety.get("id")
        out["wineBatch_designatedVariety_name"] = designated_variety.get("name")
        out["wineBatch_designatedVariety_code"] = designated_variety.get("code")
        out["wineBatch_program"] = wine_batch.get("program")
        grading = wine_batch.get("grading", {})
        out["wineBatch_grading_scaleId"] = grading.get("scaleId")
        out["wineBatch_grading_scaleName"] = grading.get("scaleName")
        out["wineBatch_grading_valueId"] = grading.get("valueId")
        out["wineBatch_grading_valueName"] = grading.get("valueName")

        # WineryBuilding
        winery_building = wd.get("wineryBuilding", {})
        out["wineryBuilding_id"] = winery_building.get("id")
        out["wineryBuilding_name"] = winery_building.get("name")

        # Volume
        volume = wd.get("volume", {})
        out["wine_volume_value"] = volume.get("value")
        out["wine_volume_unit"] = volume.get("unit")

        # Loss
        loss = wd.get("loss", {})
        loss_volume = loss.get("volume", {})
        out["wine_loss_volume_value"] = loss_volume.get("value")
        out["wine_loss_volume_unit"] = loss_volume.get("unit")
        loss_reason = loss.get("reason", {})
        out["wine_loss_reason_id"] = loss_reason.get("id")
        out["wine_loss_reason_name"] = loss_reason.get("name")

        # BottlingDetails
        out["wine_bottlingDetails"] = wd.get("bottlingDetails")

        # Weight
        weight = wd.get("weight", {})
        out["wine_weight_value"] = weight.get("value")
        out["wine_weight_unit"] = weight.get("unit")

        # Cost (object, flatten as JSON string or extract subtotals)
        cost = wd.get("cost", {})
        out["wine_cost_total"] = cost.get("total")
        out["wine_cost_average"] = cost.get("average")
        out["wine_cost_fruit"] = cost.get("fruit")
        out["wine_cost_overhead"] = cost.get("overhead")
        out["wine_cost_storage"] = cost.get("storage")
        out["wine_cost_additive"] = cost.get("additive")
        out["wine_cost_bulk"] = cost.get("bulk")
        out["wine_cost_packaging"] = cost.get("packaging")
        out["wine_cost_operation"] = cost.get("operation")
        out["wine_cost_freight"] = cost.get("freight")
        out["wine_cost_other"] = cost.get("other")

        # Allocations (array, JSON string)
        allocations = wd.get("allocations", [])
        out["wine_allocations"] = json.dumps(allocations)

        # Metrics (array, JSON string)
        metrics = wd.get("metrics", [])
        out["wine_metrics"] = json.dumps(metrics)

    return out