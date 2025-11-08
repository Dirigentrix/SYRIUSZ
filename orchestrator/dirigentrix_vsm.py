from dartrix.agents import DiagnostaVSM, StrategVSM

class DirigentrixVSM:
    """
    Orkiestrator aktywacji VSM w DARTRIX.
    """
    def run_full_analysis(self, start_step):
        diagnosta = DiagnostaVSM()
        strateg = StrategVSM()

        diagnosis = diagnosta.diagnose(start_step)
        strategy = strateg.strategize(diagnosis)

        return {
            "diagnosis": diagnosis,
            "strategy": strategy
        }