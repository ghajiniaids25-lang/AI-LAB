age = int(input("Enter Age: "))
bmi = float(input("Enter BMI: "))
bp = int(input("Enter Blood Pressure: "))
sugar = int(input("Enter Blood Sugar: "))
cholesterol = int(input("Enter Cholesterol: "))
risk_score = 0
if age >= 50:
    risk_score += 1
if bmi >= 30:
    risk_score += 2
elif bmi >= 25:
    risk_score += 1
if bp >= 140:
    risk_score += 2
elif bp >= 120:
    risk_score += 1
if sugar >= 126:
    risk_score += 2
elif sugar >= 100:
    risk_score += 1
if cholesterol >= 240:
    risk_score += 2
elif cholesterol >= 200:
    risk_score += 1
if risk_score <= 2:
    risk = "LOW RISK"
elif risk_score <= 5:
    risk = "MODERATE RISK"
else:
    risk = "HIGH RISK"
print("\n--- HEALTH RISK ANALYZER ---")
print("Risk Score:", risk_score)
print("Health Risk Level:", risk)
