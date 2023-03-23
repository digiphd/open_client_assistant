# Open Client Assistant
**Note: This project is a work in progress**
Open Client Assistant is a powerful command line chatbot designed to manage and optimize client-specific context using OpenAi GPT-4, PostgreSQL and LangChain. The chatbot allows build up a memory on clients and client projects so can get hyperelevant information when working on articles, marketing, reports, code etc. Consider it your client based personal assistant.

It was borne from my own need to quickly recall details of client work and speed up output when the confines of 8k tokens means I would loose context.

## Note, some tech skills are required. Knowing how to run a python script on your local machine and edit some of the config files.

## Features

- GPT-4 integration for advanced language understanding and generation
- PostgreSQL database for storing clients and their contexts, I use Render
- Pinecone integration for vectorized context storage and retrieval
- LangChain for memory optimization and context compression
- Handles many clients, load in the memory of each client at runtime. Conside each client a separate chat thread

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database (either local or remote)
<!-- - Pinecone API key -->
- GPT-4 API key (replace with GPT-3 API key for now)

### Installation

1. Clone the repository:

```bash
git clone git@github.com:digiphd/open_client_assistant.git
cd open_client_assistant
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your PostgreSQL database and note the connection details (host, port, user, password, and database name).

4. Configure the `config.py` file with your API keys and database credentials:

```python
OPENAPI_KEY = "your_gpt4_api_key"
# PINECONE_API_KEY = "your_pinecone_api_key"

DB_CREDENTIALS = {
    "dbname": "your_db_name",
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "your_db_host",
    "port": "your_db_port",
}
```

Replace the placeholders with your actual API keys and database credentials.

### Usage

Run the `main.py` script to start the chatbot:

```bash
python main.py
```

Follow the prompts to set the master prompt, add clients, and interact with the chatbot.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) to get started.

## One day features
1. Simple user interace
2. Advanced user interface with a talking head
3. Speech to text
4. Text to speech


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

