from ..core.dartrix_core import DartrixAgent, AgentRole

class Diagnosta(DartrixAgent):
    def __init__(self):
        super().__init__(name="Diagnosta", role=AgentRole.DIAGNOSTA, frequency="160 Hz")

    def detect_anomaly(self, data_stream):
        anomalies = [d for d in data_stream if d.get("risk_score", 0) > 0.8]
        print(f"🔍 Diagnosta wykrył {len(anomalies)} niezgodności.")
        return anomalies