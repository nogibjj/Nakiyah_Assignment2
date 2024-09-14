import pandas as pd
from io import StringIO
from main import cleanData, summaryStatistics, stackPlot, barPlot, writeToPDF
import os

"""
Test File for data processing and visualization functions
"""

# Test cleanData
def test_CleanData():
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2"""
    df = pd.read_csv(StringIO(csv_data))

    cleaned_df = cleanData(
        df, ["Gender", "Occupation", "Sleep Duration", "Quality of Sleep"], "Person ID"
    )

    # Check if DataFrame has no duplicates and contains only required columns
    assert cleaned_df.shape == (4, 4), "Duplicate removal or column filtering failed"
    assert all(
        col in cleaned_df.columns
        for col in ["Gender", "Occupation", "Sleep Duration", "Quality of Sleep"]
    ), "Column filtering failed"


# Test summaryStatistics
def test_SummaryStatistics():
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2"""
    df = pd.read_csv(StringIO(csv_data))

    summary = summaryStatistics(df)

    # Validate summary statistics for 'Sleep Duration'
    assert (
        summary.loc["mean", "Sleep Duration"] == 6.5
    ), "Mean of Sleep Duration is incorrect"
    assert (
        summary.loc["count", "Sleep Duration"] == 4
    ), "Count of Sleep Duration is incorrect"
    assert (
        summary.loc["median", "Sleep Duration"] == 6.5
    ), "Median of Sleep Duration is incorrect"

    # Validate summary statistics for 'Quality of Sleep'
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
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2
                  5,Male,Teacher,7,4"""
    df = pd.read_csv(StringIO(csv_data))

    try:
        stackPlot(df, "Sleep Duration", "Occupation")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Stack plot failed: {e}")

    assert plot_success, "Stacked plot generation failed"


# Test barPlot
def test_BarPlot():
    csv_data = """Person ID,Gender,Occupation,Sleep Duration,Quality of Sleep
                  1,Male,Engineer,7,3
                  2,Female,Doctor,6,4
                  3,Male,Engineer,8,5
                  4,Female,Lawyer,5,2
                  5,Male,Teacher,7,4
                  6,Female,Engineer,6,3"""
    df = pd.read_csv(StringIO(csv_data))

    try:
        barPlot(df, "Quality of Sleep", "Occupation", "Gender")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Bar plot failed: {e}")

    assert plot_success, "Bar plot generation failed"


# Test writeToPDF
def test_writeToPDF():
    # Mock summary statistics DataFrame
    Summary = pd.DataFrame(
        {"Metric 1": [10, 20, 30], "Metric 2": [40, 50, 60]},
        index=["Row 1", "Row 2", "Row 3"],
    )

    # Mock graph paths
    graph1 = "stack_plot.png"
    graph2 = "bar_plot.png"

    result = writeToPDF(Summary, graph1, graph2)

    # Validate PDF creation
    assert os.path.exists("summary_statistics_report.pdf"), "PDF file was not created."
    assert os.path.getsize("summary_statistics_report.pdf") > 0, "PDF file is empty."
    assert result == "PDF file created", "Unexpected result message."

    # Clean up generated PDF
    os.remove("summary_statistics_report.pdf")
    os.remove("stack_plot.png")
    os.remove("bar_plot.png")

    print("All tests passed successfully!")


# Run all tests
if __name__ == "__main__":
    test_CleanData()
    test_SummaryStatistics()
    test_StackPlot()
    test_BarPlot()
    test_writeToPDF()
