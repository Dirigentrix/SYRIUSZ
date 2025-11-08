import sys
import argparse
from dartrix.vsm import StreamBuilder
from dartrix.vsm.stream_visualizer import visualize_stream
from dartrix.orchestrator.dirigentrix_vsm import DirigentrixVSM

def main():
    parser = argparse.ArgumentParser(description="DARTRIX CLI – Value Stream Mapping")
    subparsers = parser.add_subparsers(dest="command")

    # Komenda: analyze-stream
    analyze_parser = subparsers.add_parser("analyze-stream", help="Uruchom pełną analizę VSM")
    analyze_parser.add_argument("--demo", action="store_true", help="Uruchom demo")

    # Komenda: export-map
    export_parser = subparsers.add_parser("export-map", help="Eksportuj mapę do pliku")
    export_parser.add_argument("--output", default="vsm_map", help="Nazwa pliku wyjściowego")

    args = parser.parse_args()

    if args.command == "analyze-stream" and args.demo:
        # Demo: prosty proces e-commerce
        builder = StreamBuilder()
        builder.add_step("Odbiór zamówienia", "processing", 5, True, is_start=True)
        builder.add_step("Pakowanie", "processing", 10, True)
        builder.add_step("Oczekiwanie na kuriera", "waiting", 60, False)
        builder.add_step("Wysyłka", "transport", 2, True)
        builder.connect("Odbiór zamówienia", "Pakowanie")
        builder.connect("Pakowanie", "Oczekiwanie na kuriera")
        builder.connect("Oczekiwanie na kuriera", "Wysyłka")

        start = builder.build()
        dirigent = DirigentrixVSM()
        result = dirigent.run_full_analysis(start)
        print("🔍 Diagnoza:", result["diagnosis"])
        print("💡 Strategia:", result["strategy"])

    elif args.command == "export-map":
        # Wymaga zdefiniowanego start_step — w demo użyjemy tego samego
        builder = StreamBuilder()
        builder.add_step("Start", "processing", 1, True, is_start=True)
        start = builder.build()
        path = visualize_stream(start, args.output)
        if path:
            print(f"✅ Mapa zapisana: {path}")
        else:
            print("⚠️  Brak wizualizacji — zainstaluj graphviz: pip install graphviz")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()