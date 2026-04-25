from pydantic import BaseModel


class SessionCreateRequest(BaseModel):
    theme: str


class OutlineItem(BaseModel):
    order: int
    name: str
    summary: str


class Session(BaseModel):
    id: str
    title: str
    tags: list[str]
    outline: list[OutlineItem]
