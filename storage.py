from models import Session

sessions: dict[str, Session] = {}


def save_session(session: Session) -> None:
    sessions[session.id] = session


def get_session(session_id: str) -> Session | None:
    return sessions.get(session_id)
