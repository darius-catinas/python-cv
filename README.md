# CV REST API TOOL

Check this tool in order to see some of my work.

 Works both by REST API, and also as a CLI.

 Uses the underlying flask module to expose REST endpoints and CLI commands.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cv-tool.

In order to use this, please make sure you have the latest python3 modules.

I recommend using [virtualenv](https://docs.python.org/3/library/venv.html) as the binary & dependency manager tool.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
After installing, you can run the REST API server.
```bash
flask run
```
This will expose the app on port 5000. You can change this by providing the ```--port={} ```. Use the postman collection provided in order to see how to query the endpoints.

In order to run the CLI, run 
```bash
flask print
```
This will output all the data to the standard output.
