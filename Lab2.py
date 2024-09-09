human_age = float(input("Enter human age: "))

total_dog_days = human_age * 7 * 365

dog_years = int(total_dog_days // 365)
remaining_dog_days = total_dog_days % 365    
dog_months = int(remaining_dog_days // 30)  
dog_days = int(remaining_dog_days % 30)    

cat_age_in_years = human_age / 9 
total_cat_days = cat_age_in_years * 365
cat_years = int(cat_age_in_years)
remaining_cat_days = (cat_age_in_years - cat_years) * 365
cat_months = int(remaining_cat_days // 30)
cat_days = int(remaining_cat_days % 30)

horse_age_in_years = 3 * ((human_age**2 - 47) / 7) + 12
total_horse_days = horse_age_in_years * 365
horse_years = int(horse_age_in_years)
remaining_horse_days = (horse_age_in_years - horse_years) * 365
horse_months = int(remaining_horse_days // 30)
horse_days = int(remaining_horse_days % 30)

print(f"Your age in dog years is {dog_years} years, {dog_months} months, and {dog_days} days in dog age.")
print(f"Your age in cat years is {cat_years} years, {cat_months} months, and {cat_days} days.")
print(f"Your age in horse years is {horse_years} years, {horse_months} months, and {horse_days} days.")

