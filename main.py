import json
from fastapi.responses import HTMLResponse
import uvicorn

from fastapi import Depends, FastAPI, WebSocket
import asyncio
from src.controller.log import LogController
from src.controller.cache import CacheController
from fastapi.middleware.cors import CORSMiddleware
from src.service.aws import AwsService
from src.service.jiraService import JiraServiceApi
from src.service.oracle import OracleService
from src.domain.enum.status import Status

app = FastAPI()
returnDict = {
    "Aws.SP": Status.RESOLVED.value,
    "Aws.Vi": Status.RESOLVED.value,
    "Oracle.Vi": Status.RESOLVED.value,
    "Oracle.SP": Status.RESOLVED.value,
    "Jira": Status.RESOLVED.value
}

#var ws = new WebSocket("wss://backend-hacktoon.onrender.com/ws");

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""
 
@app.get("/bruno")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(5)
        lista_jira, jira_tem_degradation = JiraServiceApi.getJiraInfo()
        simplified_infoJira = [{"provider": item["provider"], "status": item["status"]} for item in json.loads(json.dumps(lista_jira, indent=2))]
        returnDict["Jira"] = Status.DEGRADATION.value if jira_tem_degradation else Status.RESOLVED.value
        # await websocket.send_json(simplified_infoJira)

        lista_ocl, ocl_sp_tem_degradation, ocl_vi_tem_degradation = OracleService.getOracleInfo()
        simplified_infoOracle = [{"provider": item["provider"], "status": item["status"]} for item in json.loads(json.dumps(lista_ocl, indent=2))]
        
        returnDict["Oracle.Vi"] = Status.DEGRADATION.value if ocl_vi_tem_degradation else Status.RESOLVED.value
        returnDict["Oracle.SP"] = Status.DEGRADATION.value if ocl_sp_tem_degradation else Status.RESOLVED.value
        returnDict["Jira"] = Status.DEGRADATION.value if jira_tem_degradation else Status.RESOLVED.value
        await websocket.send_json(returnDict)

        # lista_aws, aws_sp_tem_degradation, aws_vi_tem_degradation = AwsService.get_AWS_log()
        # simplified_infoAWS = [{"provider": item["provider"], "status": item["status"]} for item in json.loads(json.dumps(lista_aws, indent=2))]

        # returnDict["Aws.Vi"] = Status.DEGRADATION.value if aws_vi_tem_degradation else Status.RESOLVED.value
        # returnDict["Aws.SP"] = Status.DEGRADATION.value if aws_sp_tem_degradation else Status.RESOLVED.value

        # await websocket.send_json(simplified_infoAWS)
        #TODO: Após retornar ao frontend, chamar api mongodb


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(CacheController.router)
app.include_router(LogController.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")