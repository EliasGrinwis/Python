consumptionDay = int(input("Power consumption during the day (kilowatt per hour): "))
consumptionNight = int(input("Power consumption at night (kilowatt per hour): "))
fixedCost = 83.6

invoice = "Invoice"
print(invoice)
print(len(invoice) * "*")
print("Fixed costs: €", fixedCost)
print("Daily consumption: €", consumptionDay * 0.068)
print("Night consumption: €", (consumptionNight * 0.035))
print("Total excluding VAT: €", (fixedCost + (consumptionDay * 0.068) + (consumptionNight * 0.035)))
print("Total including VAT: €", ((fixedCost + (consumptionDay * 0.068) + (consumptionNight * 0.035))) + (((fixedCost + (consumptionDay * 0.068) + (consumptionNight * 0.035)) / 100) * 21))
