# import azure.functions as func
# import asyncio
# import json
# import time

# from azurefunctions.extensions.http.fastapi import Request, StreamingResponse

# app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


# process_completed_event = asyncio.Event()
# updates = asyncio.Queue()
# is_running = False  # Flag to indicate if the process is running


# def format_message(message, is_running):
#     message = {"message": message, "is_running": is_running}
#     return f"data: {json.dumps({'message': message})}\n\n"


# async def func1(number: int):
#     global is_running, current_message
#     is_running = True
#     for i in range(1, 11):
#         current_message = f"Processing second {i}"
#         yield format_message(current_message, is_running)
#         await asyncio.sleep(1)

#     current_message = "Main function completed"
#     yield format_message(current_message, is_running)
#     yield format_message("Closing the stream", is_running)
#     is_running = False
#     yield format_message("Stream closed", is_running)
#     process_completed_event.set()


# @app.route(route="stream", methods=[func.HttpMethod.GET])
# async def stream_func1_status(req: Request) -> StreamingResponse:
#     """Endpoint to stream status messages from func1."""
#     if is_running is True:
#         return StreamingResponse(
#             "Already running",
#             media_type="text/event-stream",
#             status_code=200,
#         )
#     if is_running is False:
#         return StreamingResponse(func1(10), media_type="text/event-stream")
