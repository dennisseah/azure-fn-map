import json
import logging

import azure.functions as func
from ..libs.search import reverse_geo


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    lat = req.params.get("lat")
    lon = req.params.get("lon")
    if not lat or not lon:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a lat and lon in the query string",
            status_code=200,
        )

    return func.HttpResponse(
        json.dumps(reverse_geo(latitude=float(lat), longitude=float(lon))),
        mimetype="application/json",
    )
