# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    input = context.get_input()

    logging.info("Here in the Orchetrator")
    #logging.info(input)

    result1 = yield context.call_activity('ForChris', "hello")
    return [result1]

main = df.Orchestrator.create(orchestrator_function)