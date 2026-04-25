import uuid
from fastapi import FastAPI, HTTPException
import llm
import storage
from models import Session, SessionCreateRequest

app = FastAPI()


@app.post("/sessions", response_model=Session)
def create_session(req: SessionCreateRequest):
    outline_data = llm.generate_outline(req.theme)

    session = Session(
        id=str(uuid.uuid4()),
        title=outline_data["title"],
        tags=outline_data.get("tags", []),
        outline=[
            {"order": t["order"], "name": t["name"], "summary": t["summary"]}
            for t in outline_data.get("topics", [])
        ],
    )

    storage.save_session(session)
    return session
