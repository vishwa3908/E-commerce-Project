FROM python
WORKDIR .
COPY . .
RUN pip install -r requirement.txt
CMD python wsgi.py