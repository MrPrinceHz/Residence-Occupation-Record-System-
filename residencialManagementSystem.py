class DataEntrySystem:
    def __init__(self):
        self.data = []

    def enter_data(self, name, age, occupation):
        entry = {'Name': name, 'Age': age, 'Occupation': occupation}
        self.data.append(entry)
        print("Data entered successfully.")

    def display_data(self):
        for entry in self.data:
            print(entry)

def store_data_to_file(data, filename):
    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry['Name']}, {entry['Age']}, {entry['Occupation']}\n")

def automate_data_entry_system():
    data_system = DataEntrySystem()

    while True:
        print("\nEnter data (or type 'exit' to finish):")
        name = input("Name: ")
        if name.lower() == 'exit':
            break

        age = int(input("Age: "))
        occupation = input("Occupation: ")

        data_system.enter_data(name, age, occupation)

    print("\nEntered data:")
    data_system.display_data()

    filename = input("\nEnter filename to store data: ")
    store_data_to_file(data_system.data, filename)
    print(f"Data stored in {filename}")

if __name__ == "__main__":
    automate_data_entry_system()
