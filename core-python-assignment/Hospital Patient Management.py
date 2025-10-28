patients = []
n = int(input("Enter number of patients: "))
for i in range(n):
    print(f"\nEnter details for patient {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
search_disease = input("\nEnter disease to search for: ")
matched_patients = [p["Name"] for p in patients if p["Disease"].lower() == search_disease.lower()]
print(f"\nPatients with {search_disease}: {matched_patients}")
