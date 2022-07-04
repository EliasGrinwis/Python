weight_in_kilograms = float(input("Your weight in kilograms: "))
length_in_centimetres = int(input("Your length in centimetres: "))

#CALCULATE BMI
result = (weight_in_kilograms / (length_in_centimetres ** 2)) * 10000

#CHECK WHAT YOUR BMI IS
if result < 18:
    print("A person of", round(weight_in_kilograms, 1), "kg with a length of", length_in_centimetres, "cm has as BMI", result)
    print("This is underweight.")
if result >= 18 and result < 25:
    print("A person of", round(weight_in_kilograms, 1), "kg with a length of", length_in_centimetres, "cm has as BMI", result)
    print("This is normal weight")
if result >= 25 and result < 27:
    print("A person of", round(weight_in_kilograms, 1), "kg with a length of", length_in_centimetres, "cm has as BMI", result)
    print("This is slightly overweight")
if result >= 27 and result < 30:
    print("A person of", round(weight_in_kilograms, 1), "kg with a length of", length_in_centimetres, "cm has as BMI", result)
    print("This is moderate overweight")
if result >= 30 and result < 40:
    print("A person of", round(weight_in_kilograms, 1), "kg with a length of", length_in_centimetres, "cm has as BMI", result)
    print("This is obese")
if result >= 40:
    print("A person of", round(weight_in_kilograms, 1), "kg with a length of", length_in_centimetres, "cm has as BMI", result)
    print("This is sickly obese")
