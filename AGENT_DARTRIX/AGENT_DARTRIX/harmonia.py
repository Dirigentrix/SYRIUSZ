from ..core.dartrix_core import DartrixAgent, AgentRole

class Harmonia(DartrixAgent):
    def __init__(self):
        super().__init__(name="Harmonia", role=AgentRole.HARMONIA, frequency="196.6 Hz")

    def balance_team_mood(self, moods):
        avg = sum(moods) / len(moods) if moods else 0.5
        if avg < 0.3:
            return "Aktywuj afirmacje Mentora i herbatę po bolesnym dniu."
        return "Stan równowagi utrzymany."