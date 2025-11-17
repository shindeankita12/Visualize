import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
    path = input("Enter the path of the dataset (CSV file): ")
    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def explore_data(df):
    print("== Explore Data ==")
    print("1. Display the first 5 rows")
    print("2. Display the last 5 rows")
    print("3. Display column names")
    print("4. Display data types")
    print("5. Display basic info")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print(df.head())
    elif choice == '2':
        print(df.tail())
    elif choice == '3':
        print(df.columns.tolist())
    elif choice == '4':
        print(df.dtypes)
    elif choice == '5':
        print(df.info())
    else:
        print("Invalid choice")


def handle_missing_data(df):
    print("== Handle Missing Data ==")
    print("1. Display rows with missing values")
    print("2. Fill missing values with mean")
    print("3. Drop rows with missing values")
    print("4. Replace missing values with a specific value")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        missing = df[df.isnull().any(axis=1)]
        if missing.empty:
            print("No missing values found!")
        else:
            print(missing)

    elif choice == '2':
        df.fillna(df.mean(numeric_only=True), inplace=True)
        print("Missing values filled with mean.")

    elif choice == '3':
        df.dropna(inplace=True)
        print("Rows with missing values dropped.")

    elif choice == '4':
        value = input("Enter the value to replace missing data: ")
        df.fillna(value, inplace=True)
        print("Missing values replaced.")

    else:
        print("Invalid choice!")


def generate_statistics(df):
    print("== Descriptive Statistics ==")
    print(df.describe())


def data_visualization(df):
    print("== Data Visualization ==")
    print("1. Bar Plot")
    print("2. Line Plot")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    print("5. Histogram")
    print("6. Stack Plot")

    choice = input("Enter your choice: ")

    if choice in ['1', '2', '3', '5', '6']:
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")

        if choice == '1':
            df.plot.bar(x=x, y=y)

        elif choice == '2':
            df.plot.line(x=x, y=y)

        elif choice == '3':
            df.plot.scatter(x=x, y=y)

        elif choice == '5':
            df[y].plot.hist()

        elif choice == '6':
            df.plot.area(x=x, y=y, stacked=True)

    elif choice == '4':
        col = input("Enter column name for pie chart: ")
        df[col].value_counts().plot.pie(autopct='%1.1f%%')

    else:
        print("Invalid choice!")
        return None

    plt.tight_layout()
    plt.show()
    return plt


def save_visualization(plt_obj):
    filename = input("Enter file name to save the plot (e.g., plot.png): ")
    plt_obj.savefig(filename)
    print(f"Visualization saved as {filename}")


def main():
    df = None
    plt_obj = None

    while True:
        print("\n========= Data Analysis & Visualization Program =========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            df = load_dataset()

        elif choice == '2':
            if df is not None:
                explore_data(df)
            else:
                print("Please load a dataset first!")

        elif choice == '3':
            print("Feature not implemented yet.")

        elif choice == '4':
            if df is not None:
                handle_missing_data(df)
            else:
                print("Please load a dataset first!")

        elif choice == '5':
            if df is not None:
                generate_statistics(df)
            else:
                print("Please load a dataset first!")

        elif choice == '6':
            if df is not None:
                plt_obj = data_visualization(df)
            else:
                print("Please load a dataset first!")

        elif choice == '7':
            if plt_obj is not None:
                save_visualization(plt_obj)
            else:
                print("No plot to save yet!")

        elif choice == '8':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

            
if __name__ == "__main__":
    main()