#!/bin/shell

if (systemctl -q is-active nginx) 
then
    echo "Nginx is runned!";
else
    echo "Nginx is stoped. Running nginx...";
    systemctl start nginx;
fi

if [[ $# -eq 0 ]] 
then
    echo "Arguments is empty!";
    exit 1;
else
    poetry run python -m gunicorn --workers=$1 --bind=localhost:$2 app:app
fi

