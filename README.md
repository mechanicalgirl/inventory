Create a virtual environment:
-----------------------------

```python
cd ~/path/to/inventory/
virtualenv -p python3 inventory-env
source inventory-env/bin/activate
```

To run locally:
---------------

```python
cd ~/path/to/inventory/
source inventory-env/bin/activate
pip install -r requirements.txt
cd inventory
python3 manage.py migrate
python3 manage.py runserver
```

To create a superuser (for admin access):
-----------------------------------------

```python
cd ~/path/to/inventory/inventory/
python3 manage.py createsuperuser
```

To view the admin:
------------------

http://127.0.0.1:8000/admin/
