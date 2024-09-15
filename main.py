import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Function reading the csv file
def readData(df):
    return pd.read_csv(df)


# Function cleaning the data
def cleanData(df, Columns, Duplicate):
    dfCleaned = df.drop_duplicates(subset=Duplicate, keep="first")
    dfCleaned = dfCleaned[Columns]
    return dfCleaned


# Creating Summary Statistics
def summaryStatistics(df):
    SumStats = df.describe(exclude=["O"]).reset_index()
    Median = df.median(numeric_only=True)
    Median_df = pd.DataFrame(Median).T  # Transpose to match the structure of SumStats
    SumStats = pd.concat([SumStats, Median_df], ignore_index=True)
    SumStats.fillna("median", inplace=True)
    SumStats.set_index("index", inplace=True)
    return SumStats


# Creating a Stacked Plot
def stackPlot(df, xVal, StackVal):
    PivotData = df.groupby([xVal, StackVal]).size().unstack().fillna(0)
    PivotData.plot(kind="bar", stacked=True, figsize=(12, 8), colormap="tab20")
    plt.title(f"Distribution of {StackVal} by {xVal}")
    plt.xlabel(f"{xVal}")
    plt.ylabel("Count")
    plt.legend(title=f"{StackVal}", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig("stack_plot.png")
    plt.close()
    return "stack_plot.png"


# Creating a Box Plot
def barPlot(df, xVal, yVal, Segregate):
    GroupingData = df.groupby([yVal, Segregate])[xVal].mean().unstack()
    GroupingData.plot(kind="barh", color=["#FFD0EC", "#E59BE9"])
    plt.xlabel(f"Average {xVal}")
    plt.ylabel(f"{yVal}")
    plt.title(f"Average {xVal} by {yVal} and {Segregate}")
    plt.legend(title="Gender", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig("bar_plot.png")
    plt.close()
    return "bar_plot.png"


def writeToPDF(Summary, graph1, graph2):

    # Writing data into PDF
    pdf = FPDF(format="letter")
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # Add Title
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Summary Statistics", ln=True, align="C")
    pdf.ln(10)

    # Add Summary Statistics as a Table
    page_width = 190  # Approximate width of the PDF page after margins
    col_width = page_width / (
        len(Summary.columns) + 1
    )  # Divide width equally among all columns

    # Add headers
    pdf.set_font("Times", "B", 12)
    pdf.cell(col_width, 10, "Metric", border=1)
    for col in Summary.columns:
        pdf.cell(col_width, 10, col, border=1)
    pdf.ln()

    # Add rows for each metric
    pdf.set_font("Times", size=12)
    for i, row in Summary.iterrows():
        pdf.cell(col_width, 10, str(i), border=1)
        for col in Summary.columns:
            pdf.cell(col_width, 10, str(row[col]), border=1)
        pdf.ln()

    # Add Plots to PDF
    # Add Stacked Plot to PDF
    pdf.add_page()
    pdf.ln(10)
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Stacked Plot", ln=True, align="C")
    pdf.ln(10)
    pdf.image(graph1, x=10, y=pdf.get_y(), w=180)
    pdf.ln(10)

    # Add Bar Plot to PDF
    pdf.add_page()
    pdf.set_font("Times", "B", 14)
    pdf.cell(200, 10, txt="Bar Plot", ln=True, align="C")
    pdf.ln(10)
    pdf.image(graph2, x=10, y=pdf.get_y(), w=180)

    # Save PDF
    pdf.output("summary_statistics_report.pdf")
    return "PDF file created"


# Initializing Variables
Dataset = "Sleep_health_and_lifestyle_dataset.csv"
RequiredColumns = ["Gender", "Occupation", "Sleep Duration", "Quality of Sleep"]

DuplicateValues = "Person ID"
Gender = "Gender"
Occupation = "Occupation"
SleepHours = "Sleep Duration"
SleepQuality = "Quality of Sleep"

# Calling Functions
Data = readData(Dataset)
CleanData = cleanData(Data, RequiredColumns, DuplicateValues)
SummaryStatistics = summaryStatistics(CleanData)
StackPlot = stackPlot(CleanData, SleepHours, Occupation)
BarPlot = barPlot(CleanData, SleepQuality, Occupation, Gender)
Output = writeToPDF(SummaryStatistics, StackPlot, BarPlot)

print(SummaryStatistics)
print("Everything works great!")
