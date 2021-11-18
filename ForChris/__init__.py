# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
 
import logging
import json

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)

    #Premade above
    environment = req.params.get('environment')
    filename = req.params.get('filename')
    api = req.params.get('api')
    payload = req.get_body().decode('utf-8')

    logging.info("-------------- after decode ------------------")


    ctx = {
        'payload': payload,
        'environment': environment,
        'filename': filename,
        'api': api
    }

    ctx = json.dumps(ctx)
    
    instance_id = await client.start_new(req.route_params["functionName"], client_input= payload)
 

    #Premade stuff Below

    #instance_id = await client.start_new(req.route_params["functionName"], None, None)

    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    return client.create_check_status_response(req, instance_id)