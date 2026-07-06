import pytest
import os
import sqlite3
import database as db

# Use a test database
db.DB_NAME = "test_eco_buddy.db"

@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup
    if os.path.exists(db.DB_NAME):
        os.remove(db.DB_NAME)
    db.init_energy_db()
    yield
    # Teardown
    if os.path.exists(db.DB_NAME):
        os.remove(db.DB_NAME)

def test_add_and_get_appliance():
    # Test adding an appliance
    success = db.add_appliance("Test AC", "AC", 2, 1500, 5, 10)
    assert success is True

    # Test getting appliances
    appliances = db.get_appliances()
    assert len(appliances) == 1
    assert appliances[0]['name'] == "Test AC"
    assert appliances[0]['category'] == "AC"
    assert appliances[0]['quantity'] == 2
    assert appliances[0]['power_rating_watts'] == 1500
    assert appliances[0]['hours_used_per_day'] == 5
    assert appliances[0]['standby_draw_watts'] == 10

def test_delete_appliance():
    db.add_appliance("Test Heater", "Heat Pump", 1, 2000, 4, 0)
    appliances = db.get_appliances()
    app_id = appliances[0]['id']
    
    success = db.delete_appliance(app_id)
    assert success is True
    
    appliances_after = db.get_appliances()
    assert len(appliances_after) == 0

def test_save_and_get_solar_config():
    success = db.save_solar_config(50.0, 5.0, 0.12, 22.0, 2000.0, 150.0, 2.5)
    assert success is True
    
    config = db.get_solar_config()
    assert config is not None
    assert config['roof_space_m2'] == 50.0
    assert config['peak_sun_hours'] == 5.0
    assert config['utility_rate_per_kwh'] == 0.12
    assert config['panel_efficiency'] == 22.0
    assert config['installation_cost_per_kw'] == 2000.0
    assert config['maintenance_cost_per_year'] == 150.0
    assert config['annual_rate_increase'] == 2.5
