import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app import app

def test_upload_page():

    client = app.test_client()

    response = client.get("/upload")

    assert response.status_code == 200


def test_dashboard_page():

    client = app.test_client()

    response = client.get("/dashboard")

    assert response.status_code == 200


def test_abc_page():

    client = app.test_client()

    response = client.get("/abc-analysis")

    assert response.status_code == 200


def test_forecasting_page():

    client = app.test_client()

    response = client.get("/forecasting")

    assert response.status_code == 200


def test_reorder_page():

    client = app.test_client()

    response = client.get("/reorder-point")

    assert response.status_code == 200


def test_api():

    client = app.test_client()

    response = client.get("/api/inventory")

    assert response.status_code == 200

    assert response.content_type == "application/json"