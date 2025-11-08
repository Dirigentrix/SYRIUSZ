from ..core.dartrix_core import DartrixAgent, AgentRole

class AsyncAgent(DartrixAgent):
    """Przekształca spotkania w tryb asynchroniczny"""
    def __init__(self):
        super().__init__(name="Async", role=AgentRole.ASYNC, frequency="152 Hz")

    def convert_meeting(self, transcript):
        summary = "Podsumowanie asynchroniczne: " + transcript[:100] + "..."
        print("⏱️ Async: Spotkanie przekształcone w dokument.")
        return summary