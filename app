server {
	listen 80;
	server_name 34.228.249.14;
	location / {
		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/my_first_big_project/app.sock;
		}
}
