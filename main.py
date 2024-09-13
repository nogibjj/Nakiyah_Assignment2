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
    print(Median_df)
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
    plt.show()
    return "Stacked Plot"


# Creating a Box Plot
def barPlot(df, xVal, yVal, Segregate):
    GroupingData = df.groupby([yVal, Segregate])[xVal].mean().unstack()
    GroupingData.plot(kind="barh", color=["#FFD0EC", "#E59BE9"])
    plt.xlabel(f"Average {xVal}")
    plt.ylabel(f"{yVal}")
    plt.title(f"Average {xVal} by {yVal} and {Segregate}")
    plt.legend(title="Gender", loc="best")
    plt.tight_layout()
    plt.show()
    return "Bar Graph"


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
PlotStacked = stackPlot(CleanData, SleepHours, Occupation)
BarPlot = barPlot(CleanData, SleepQuality, Occupation, Gender)

## Writing data into pdf

# Initialize PDF
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Title
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Summary Statistics", ln=True, align='C')
pdf.ln(10)

# Add Summary Statistics
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="Summary Statistics:\n")
for col in SummaryStatistics.columns:
    pdf.cell(0, 10, txt=f"{col}: {SummaryStatistics[col].to_list()}", ln=True)

# Add Plots to PDF
pdf.ln(10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Stacked Plot", ln=True, align='C')
pdf.ln(10)

# Save Stacked Plot to file
stack_plot_file = "stack_plot.png"
stackPlot(CleanData, SleepHours, Occupation)
plt.savefig(stack_plot_file)
plt.close()

# Add Stacked Plot to PDF
pdf.image(stack_plot_file, x=10, y=pdf.get_y(), w=180)
pdf.ln(10)

pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Bar Plot", ln=True, align='C')
pdf.ln(10)

# Save Bar Plot to file
bar_plot_file = "bar_plot.png"
barPlot(CleanData, SleepQuality, Occupation, Gender)
plt.savefig(bar_plot_file)
plt.close()

# Add Bar Plot to PDF
pdf.image(bar_plot_file, x=10, y=pdf.get_y(), w=180)

# Save PDF
pdf.output("summary_statistics_report.pdf")