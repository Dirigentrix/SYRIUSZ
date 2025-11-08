class ProcessStep:
    """
    Reprezentuje pojedynczy krok w Value Stream Map.
    """
    def __init__(self, name: str, step_type: str, time: float, value_added: bool):
        self.name = name
        self.type = step_type  # np. "processing", "waiting", "transport"
        self.time = time  # czas trwania w minutach
        self.value_added = value_added
        self.next_steps = []

    def add_next(self, step):
        """Dodaje następny krok do ścieżki."""
        if isinstance(step, ProcessStep):
            self.next_steps.append(step)
        else:
            raise TypeError("Next step must be a ProcessStep instance.")