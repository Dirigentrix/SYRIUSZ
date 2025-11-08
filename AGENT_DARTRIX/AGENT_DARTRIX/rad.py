from ..core.dartrix_core import DartrixAgent, AgentRole

class RAD(DartrixAgent):
    """Routing & Dialogue — koordynator komunikacji"""
    def __init__(self):
        super().__init__(name="RAD", role=AgentRole.RAD, frequency="174 Hz")

    def route_message(self, sender, receiver, content):
        print(f"📡 RAD: Wiadomość od {sender} do {receiver} — przekazana.")
        return {"status": "routed", "timestamp": __import__("datetime").datetime.utcnow().isoformat()}