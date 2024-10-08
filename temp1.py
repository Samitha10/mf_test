# def generate_sensor_data():
#     """Generate real-time sensor data."""
#     for i in range(10):
#         # Simulate temperature and humidity readings
#         temperature = 20 + i
#         humidity = 50 + i
#         yield f"data: {{'temperature': {temperature}, 'humidity': {humidity}}}\n\n"
#         time.sleep(1)


# @app.route(route="stream1", methods=[func.HttpMethod.GET])
# async def stream_sensor_data1(req: Request) -> StreamingResponse:
#     """Endpoint to stream real-time sensor data."""
#     return StreamingResponse(generate_sensor_data(), media_type="text/event-stream")


"""@app.function_name(name="HttpTrigger2")
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully."
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )
"""

""" @app.function_name(name="HttpTrigger1")
@app.route(route="hello")
async def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    for i in range(1, 4):
        message = f"Hello, {i}. This HTTP triggered function executed successfully."
        logging.info(message)
        await asyncio.sleep(1)
    return func.HttpResponse("Hello world")
 """
