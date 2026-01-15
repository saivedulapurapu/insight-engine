from src.engine.insight_engine import generate_insights

print("📊 Insight Engine Output:\n")

for insight in generate_insights():
    print("Insight:", insight)
