import os
import sys

def init_local_instance():
    """Inicjuje lokalną instancję DARTRIX w bieżącym katalogu."""
    dirs = [
        "local/data",
        "local/logs",
        "local/config"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"✅ Utworzono: {d}")

    with open("local/config/dartrix.yaml", "w", encoding="utf-8") as f:
        f.write("""# Konfiguracja lokalna DARTRIX
vsm:
  default_unit: "minutes"
  visualization: "graphviz"
security:
  api_keys_local_only: true
""")

    print("\n🌀 Lokalna instancja DARTRIX gotowa.")
    print("📁 Dane i klucze będą przechowywane tylko lokalnie.")

if __name__ == "__main__":
    init_local_instance()