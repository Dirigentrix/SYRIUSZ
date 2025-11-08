from dartrix.vsm.stream_analyzer import analyze_stream

class DiagnostaVSM:
    """
    Agent Diagnosta VSM — identyfikuje straty i generuje raport.
    """
    def diagnose(self, start_step):
        metrics = analyze_stream(start_step)
        report = {
            "status": "success",
            "metrics": metrics,
            "recommendations": []
        }

        if metrics["waste_time"] > metrics["value_time"]:
            report["recommendations"].append("Wysoki poziom strat — rozważ eliminację kroków nie tworzących wartości.")
        if metrics["value_ratio"] < 0.3:
            report["recommendations"].append("Niska efektywność — zoptymalizuj procesy kluczowe.")

        return report