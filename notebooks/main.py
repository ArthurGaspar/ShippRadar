# Importando dados

import pandas as pd
import numpy as np

# Gerando dados
driver_table = pd.DataFrame({
    "driver_id": ["d1001001"],
    "admission_date": ["01/05/2020"],
    "age": [37]
})

pickup_stop_table = pd.DataFrame({
    "pickup_stop_id": [1],
    "address_id": ["ad1"],
    "route_id": ["r13"],
    "schedule_date": ["23/05/2025 05:00"],
    "limit_date": ["24/05/2025 12:00"],
    "real_ops": ["23/05/2025 07:48"]
})

delivery_stop_table = pd.DataFrame({
    "delivery_stop_id": [2],
    "address_id": ["ad2"],
    "route_id": ["r13"],
    "scheduled_date" : ["23/05/2025 11:00"],
    "limit_date": ["24/05/2025 18:00"],
    "real_ops": ["23/05/2025 14:59:00"]
})

route_table = pd.DataFrame({
    "route_id": ["r13"],
    "status": ["Completed"],
    "driver_id": ["d1001001"],
    "preditive_risk": [0.7],
    "scheduled_date": ["24/05/2025 12:00"],
    "limit_date": ["24/05/2025 18:00"],
    "start_ops": ["23/05/2025 07:48"],
    "end_ops": ["23/05/2025 14:59"],
    "date_created": ["22/05/2025 16:00"]
})

address_table = pd.DataFrame({
    "address_id": ["ad1", "ad2"],
    "address": ["Rua flores", "Rua margaridas"],
    "number": [52, 161],
    "neighborhood": ["Guaianases", "Bem longe"],
    "city": ["São Paulo", "Caieiras"],
    "latitude": [-23.5766, -23.3751],
    "longitude": [-46.4097, -46.7265],
    "postal_code": [847271, 286291]
})

package_table = pd.DataFrame({
    "package_id": ["p582"],
    "package_name": ["Petz Package"],
    "package_quantity": [2],
    "package_size": ["GG"],
    "package_weight": [58],
    "package_value": [30000.00],
    "volume": [58],
    "pickup_stop_id": [1],
    "delivery_stop_id": [2],
    "route_id": ["r13"],
    "vehicle_id": ["v1001001"]
})

vehicle_table = pd.DataFrame({
    "vehicle_id": ["v1001001"],
    "license_plate": ["ABC-1234"],
    "model": ["Fiat Uno"],
    "driver_id": ["d1001001"],
    "vehicle_type": ["car"]
})

incidence_table = pd.DataFrame({
    "incidence_id": ["i1001001-1"],
    "incidence_code": ["licenseFine"],
    "driver_id": ["d1001001"],
    "weight": [0.1],
    "date": ["14/02/2025"],
    "status": ["Resolved"]
})

