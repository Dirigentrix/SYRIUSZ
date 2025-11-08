from collections import deque

def analyze_stream(start_step):
    """
    Analizuje Value Stream Map począwszy od danego kroku.
    Zwraca metryki: całkowity czas, czas wartości dodanej, czas strat.
    """
    if not start_step:
        raise ValueError("Start step cannot be None.")

    total_time = 0
    value_time = 0
    visited = set()
    queue = deque([start_step])

    while queue:
        step = queue.popleft()
        if id(step) in visited:
            continue
        visited.add(id(step))

        total_time += step.time
        if step.value_added:
            value_time += step.time

        queue.extend(step.next_steps)

    return {
        "total_time": total_time,
        "value_time": value_time,
        "waste_time": total_time - value_time,
        "value_ratio": round(value_time / total_time, 3) if total_time > 0 else 0
    }