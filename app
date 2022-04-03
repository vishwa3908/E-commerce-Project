server {
	listen 80;
	server_name 54.227.27.58;
	location / {
		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/my_first_big_project/app.sock;
		}
}
