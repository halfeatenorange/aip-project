FROM python:3.9
WORKDIR /notebooks
RUN pip install --no-cache-dir --upgrade jupyterlab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]