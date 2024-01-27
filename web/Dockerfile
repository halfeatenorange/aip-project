FROM python:3.9
ENV GRADIO_SERVER_NAME=0.0.0.0
ENV GRADIO_SERVER_PORT=7860
WORKDIR /app
RUN pip install --no-cache-dir --upgrade gradio
COPY ./src /app
CMD ["python", "main.py"]