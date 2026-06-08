# Airbus Inventory Intelligence Dashboard

GIT repo link
https://github.com/shashankdec1/airbus-inventory-intelligence.git


## Overview

The Airbus Inventory Intelligence Dashboard is a Flask-based web application designed to help organizations manage and analyze inventory data efficiently. The application allows users to upload inventory datasets, perform inventory classification, forecast future demand, calculate reorder points, and access inventory information through a REST API.

This project demonstrates the integration of front-end and back-end web development using Python and Flask while applying inventory management concepts in a practical business scenario.

---

## Features

### Inventory Upload

* Upload inventory data using CSV files.
* Store and process inventory records.

### Inventory Dashboard

* View inventory information in a structured dashboard.
* Monitor stock levels and inventory status.

### ABC Analysis

* Classify inventory items into A, B, and C categories based on inventory value.
* Identify high-priority inventory items.

### Demand Forecasting

* Estimate future inventory demand using historical demand data.
* Support inventory planning and decision-making.

### Reorder Point Calculation

* Calculate reorder points using demand and lead-time information.
* Help prevent stock shortages and improve inventory control.

### REST API

* Provide inventory data through a JSON API endpoint.
* Enable integration with external systems.

---

## Technology Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Pandas
* HTML
* CSS
* Docker
* Git & GitHub

---

## Project Structure

```text
airbus-inventory-intelligence-main/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── sample_inventory.csv
├── generate_inventory.py
│
├── templates/
├── static/
├── tests/
├── instance/
└── screenshots/
```

---

## Application Routes

| Route          | Description                       |
| -------------- | --------------------------------- |
| /upload        | Upload inventory dataset          |
| /dashboard     | Inventory dashboard               |
| /abc-analysis  | Inventory classification analysis |
| /forecasting   | Demand forecasting                |
| /reorder-point | Reorder point calculation         |
| /api/inventory | Inventory API endpoint            |

---

## API Endpoint

### Get Inventory Data

```text
GET /api/inventory
```

Example JSON Response:

```json
[
  {
    "part_number": "A100",
    "part_name": "Wing Bolt",
    "current_stock": 150
  }
]
```

---

## Running the Application Locally

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python3 app.py
```

Open the application in your browser:

```text
http://localhost:5001
```

---

## Running with Docker

Build and run the application using Docker Compose:

```bash
docker compose up --build
```

Open:

```text
http://localhost:5001
```

---

## Testing

Run automated tests:

```bash
pytest
```

---

## Screenshots

Add screenshots of the application inside a `screenshots` folder and reference them here.

### Upload Page

![Upload Page](screenshots/upload-page.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

### ABC Analysis

![ABC Analysis](screenshots/abc-analysis.png)

### Forecasting

![Forecasting](screenshots/forecasting.png)

### Reorder Point

![Reorder Point](screenshots/reorder-point.png)

---

## Team Collaboration

This project was developed collaboratively using Git and GitHub for version control, code integration, and project management.

---

## Future Improvements

* Advanced forecasting models
* Authentication and user management
* Interactive data visualizations
* Cloud deployment on AWS or Azure
* Enhanced inventory analytics

---

## License

This project was developed for academic purposes as part of a Python Web Application Development course.