"""Entrypoint for docker"""

python3 manage.py collectstatic
python3 manage.py migrate