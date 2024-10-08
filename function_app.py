import azure.functions as func
import asyncio
import json
import time

from azurefunctions.extensions.http.fastapi import (
    Request,
    StreamingResponse,
    HTMLResponse,
)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

process_completed_event = asyncio.Event()
updates = asyncio.Queue()
is_running = False  # Flag to indicate if the process is running


def format_message(message, is_running):
    message = {"message": message, "is_running": is_running}
    return json.dumps(message)


async def func1(number: int):
    global is_running, current_message
    is_running = True
    for i in range(1, 11):
        current_message = f"Processing second is {i}"
        await updates.put(format_message(current_message, is_running))
        await asyncio.sleep(1)

    current_message = "Main function completed"
    await updates.put(format_message(current_message, is_running))
    await updates.put(format_message("Closing the stream : ", is_running))
    is_running = False
    await updates.put(format_message("Stream closed", is_running))
    process_completed_event.set()


@app.route(route="start-func1", methods=[func.HttpMethod.GET])
async def start_func1(req: Request) -> HTMLResponse:
    """Endpoint to start func1."""
    if not is_running:
        process_completed_event.clear()
        asyncio.create_task(func1(10))
        return HTMLResponse("func1 started.")
    else:
        return HTMLResponse("func1 is already running.", status_code=400)


@app.route(route="stream-status", methods=[func.HttpMethod.GET])
async def stream_func1_status(req: Request) -> StreamingResponse:
    """Endpoint to stream status messages from func1."""

    async def event_generator():
        while not process_completed_event.is_set() or not updates.empty():
            message = await updates.get()
            yield message

    return StreamingResponse(event_generator(), media_type="text/event-stream")
