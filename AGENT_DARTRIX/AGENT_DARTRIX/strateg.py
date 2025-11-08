from ..core.dartrix_core import DartrixAgent, AgentRole

class Strateg(DartrixAgent):
    def __init__(self):
        super().__init__(name="Strateg", role=AgentRole.STRATEG, frequency="165.2 Hz")

    def propose_improvement(self, issue):
        improvements = {
            "wysokie_straty": "Zastosuj metodę 5S w strefach oczekiwania.",
            "niska_efektywnosc": "Wprowadź automatyzację w krokach manualnych.",
            "brak_motywacji": "Aktywuj rytuał afirmacji z Mentorem."
        }
        return improvements.get(issue, "Przeprowadź retrospektywę z Cieniem.")