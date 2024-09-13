import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from main import readData, cleanData, summaryStatistics, stackPlot, barPlot

"""
Test File for data processing and visualization functions
"""

# Test cleanData
def test_CleanData():
    # Define the dummy DataFrame directly inside the function
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2"""

    df = pd.read_csv(StringIO(csv_data))

    RequiredColumns = ["Gender", "Occupation", "Sleep Duration", "Quality of Sleep"]
    DuplicateValues = "Person ID"

    cleaned_df = cleanData(df, RequiredColumns, DuplicateValues)

    # Check if the cleaned DataFrame has no duplicates and contains only required columns
    assert cleaned_df.shape == (
        4,
        len(RequiredColumns),
    ), "Duplicate removal or column filtering failed"
    assert all(
        col in cleaned_df.columns for col in RequiredColumns
    ), "Column filtering failed"


# Test summaryStatistics
def test_SummaryStatistics():
    # Define the dummy DataFrame directly inside the function
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2"""

    df = pd.read_csv(StringIO(csv_data))

    summary = summaryStatistics(df)
    print(summary)

    # Check if the summary statistics contain the required metrics for 'Sleep Duration'
    assert (
        summary.loc["mean", "Sleep Duration"] == 6.5
    ), "Mean of Sleep Duration is incorrect"
    assert (
        summary.loc["count", "Sleep Duration"] == 4
    ), "Count of Sleep Duration is incorrect"
    assert (
        summary.loc["median", "Sleep Duration"] == 6.5
    ), "Median of Sleep Duration is incorrect"

    # Check if the summary statistics contain the required metrics for 'Quality of Sleep'
    assert (
        summary.loc["mean", "Quality of Sleep"] == 3.5
    ), "Mean of Quality of Sleep is incorrect"
    assert (
        summary.loc["count", "Quality of Sleep"] == 4
    ), "Count of Quality of Sleep is incorrect"
    assert (
        summary.loc["median", "Quality of Sleep"] == 3.5
    ), "Median of Quality of Sleep is incorrect"


# Test stackPlot
def test_StackPlot():
    # Define the dummy DataFrame directly inside the function
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2
                  5,Male,Teacher,7,4"""

    df = pd.read_csv(StringIO(csv_data))

    try:
        # Test plot, but not displaying it
        stackPlot(df, "Sleep Duration", "Occupation")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Stack plot failed: {e}")

    assert plot_success, "Stacked plot generation failed"


# Test barPlot
def test_BarPlot():
    # Define the dummy DataFrame directly inside the function
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2
                  5,Male,Teacher,7,4
                  6,Female,Engineer,6,3"""

    df = pd.read_csv(StringIO(csv_data))

    try:
        # Test plot, but not displaying it
        barPlot(df, "Quality of Sleep", "Occupation", "Gender")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Bar plot failed: {e}")

    assert plot_success, "Bar plot generation failed"


# Run all tests
if __name__ == "__main__":
    test_CleanData()
    test_SummaryStatistics()
    test_StackPlot()
    test_BarPlot()

