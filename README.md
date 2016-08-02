Create a virtual environment:
-----------------------------

```python
cd ~/path/to/etsysell/
virtualenv -p python3 etsysell-env
source etsysell-env/bin/activate
```

To run locally:
---------------

```python
cd ~/path/to/etsysell/
source etsysell-env/bin/activate
pip install -r requirements.txt
cd etsysell
python3 manage.py migrate
python3 manage.py runserver
```

To create a superuser (for admin access):
-----------------------------------------

```python
cd ~/path/to/etsysell/etsysell/
python3 manage.py createsuperuser
```

To view the admin:
------------------

http://127.0.0.1:8000/admin/
