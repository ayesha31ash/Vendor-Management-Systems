Vendor Management System

Welcome to the Vendor Management System repository, a powerful and comprehensive system developed using Django and Django REST Framework. The primary objective of this system is to efficiently manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

Objective:

Develop a Vendor Management System with the following core features:

Core Features:

Vendor Profile Management:

Model Design:

Create a robust model to store vendor information, including name, contact details, address, and a unique vendor code.

API Endpoints:

POST /api/vendors/: Create a new vendor.

GET /api/vendors/: List all vendors.

GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.

PUT /api/vendors/{vendor_id}/: Update a vendor's details.

DELETE /api/vendors/{vendor_id}/: Delete a vendor.

Purchase Order Tracking:

Model Design:

Track purchase orders with fields like PO number, vendor reference, order date, items, quantity, and status.

API Endpoints:

POST /api/purchase_orders/: Create a purchase order.

GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.

GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.

PUT /api/purchase_orders/{po_id}/: Update a purchase order.

DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

Go to the project directory

  cd vendor_management_project
Create Virtual Environment

  py -m venv venv   #install virtual enviroment
  
  venv\scripts\activate   #activate virtual enviroment venv
Install

  pip install -r requirements.txt #install required packages
  py manage.py migrate # run first migration
Start the server

  python manage.py runserver # run the server


  Usage
  
To use the vendor_management_project, follow these steps:

Access the system via the provided URL (e.g., http://127.0.0.1:8000/ ).

    http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/vendors/
Create a new vendor. ● GET /api/vendors/: List all vendors. ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details. ● PUT /api/vendors/{vendor_id}/: Update a vendor's details. ● DELETE /api/vendors/{vendor_id}/: Delete a vendor. as needed.

