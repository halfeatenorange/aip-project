# aip-project

## Running Instructions

There are 3 services defined in `docker-compose.yml`
1. `api`: This creates the FastAPI service used to query the LLM
2. `web`: This creates the gradio chatbot frontend used to communicate with the `api`, and chat with the llm
3. `notebook-dev`: This launches a jupyterlab instance, in which you can navigate to `Test API.ipynb` to view the outputs from the api calls. Alternatively, you can add your own prompts to this notebook to generate some LLM outputs.

To bring up the services, run `docker-compose up -d`. 
1. `api`: The api will be available at `localhost:80`
2. `web`: The chatbot interface will be available at `localhost:7860`
3. `notebook-dev`: The notebook will be available at `localhost:8888`. You will need a token (see docker logs of the `notebook-dev` container) to login to the notebook.

## Demo

### API:
To view or play around with the API outputs, navigate to `Test API.ipynb`. Some outputs have been added here for convenience of viewing:

<Add in Generate>

<Add in Generate Stream>

### Chatbot
A gradio interface had been built for a more interactive experience with the LLM. To play with the chatbot, visit `localhost:7860` after bringing up the docker containers. A short video demo is provided:

<Add in video demo>