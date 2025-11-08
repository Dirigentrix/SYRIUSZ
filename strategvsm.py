class StrategVSM:
    """
    Agent Strateg — proponuje usprawnienia na podstawie diagnostyki.
    """
    def strategize(self, diagnosis_report):
        improvements = []
        if "Wysoki poziom strat" in str(diagnosis_report.get("recommendations", [])):
            improvements.append("Zastosuj metodę 5S w strefach oczekiwania.")
        if "Niska efektywność" in str(diagnosis_report.get("recommendations", [])):
            improvements.append("Wprowadź automatyzację w krokach manualnych.")
        return {
            "improvements": improvements,
            "priority": "high" if len(improvements) > 1 else "medium"
        }