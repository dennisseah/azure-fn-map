import json
import logging

import azure.functions as func
from ..libs.search import address as addr_search


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    query = req.params.get("query")
    if not query:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a query in the query string",
            status_code=200,
        )

    return func.HttpResponse(json.dumps(addr_search(query)), mimetype="application/json")
