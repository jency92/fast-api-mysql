From python
ADD ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
ADD ./main.py /
ENTRYPOINT ["python3", "main.py"]
 
