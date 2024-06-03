FROM python 

WORKDIR /main

COPY . .

RUN pip install flask
RUN pip install openai==0.28

EXPOSE 8080

CMD [ "python", "main.py"]