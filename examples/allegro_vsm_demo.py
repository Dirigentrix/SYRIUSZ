from dartrix.vsm import StreamBuilder
from dartrix.orchestrator.dirigentrix_vsm import DirigentrixVSM

def allegro_order_vsm():
    """Demo: typowy proces realizacji zamówienia na Allegro."""
    builder = StreamBuilder()
    builder.add_step("Zamówienie otrzymane", "system", 0.5, False, is_start=True)
    builder.add_step("Weryfikacja płatności", "processing", 2, True)
    builder.add_step("Przygotowanie do pakowania", "waiting", 30, False)
    builder.add_step("Pakowanie", "processing", 8, True)
    builder.add_step("Nadanie przesyłki", "transport", 5, True)
    builder.add_step("Oczekiwanie na odbiór", "waiting", 1440, False)  # 1 dzień

    builder.connect("Zamówienie otrzymane", "Weryfikacja płatności")
    builder.connect("Weryfikacja płatności", "Przygotowanie do pakowania")
    builder.connect("Przygotowanie do pakowania", "Pakowanie")
    builder.connect("Pakowanie", "Nadanie przesyłki")
    builder.connect("Nadanie przesyłki", "Oczekiwanie na odbiór")

    start = builder.build()
    dirigent = DirigentrixVSM()
    result = dirigent.run_full_analysis(start)

    print("📦 Analiza zamówienia Allegro:")
    print(f"⏱️  Całkowity czas: {result['diagnosis']['metrics']['total_time']} min")
    print(f"✅ Czas wartości dodanej: {result['diagnosis']['metrics']['value_time']} min")
    print(f"🗑️  Straty: {result['diagnosis']['metrics']['waste_time']} min")
    print(f"💡 Rekomendacje: {result['diagnosis']['recommendations']}")
    print(f"🚀 Usprawnienia: {result['strategy']['improvements']}")

if __name__ == "__main__":
    allegro_order_vsm()