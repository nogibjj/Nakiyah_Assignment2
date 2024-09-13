# Nakiyah Dhariwala - Assignment 2
# Week 2

In the first assignment, we developed a Python template incorporating best practices for organizing a Python project. For this second assignment, we will build on that template to write a Python script that reads a CSV file, utilizes Pandas to generate descriptive statistics, and produces both statistical outputs and visualizations.

## Repository contents:
1. .devcontainer directory (a) devcontainer.json (b) Dockerfile
2. .github/worflows/cicd.yml --> this is configuration file that defines the steps necessary to build, test, and deploy an application.
3. .gitignore --> to ensure some cache files like "pychache" do not get pushed to the github repo.
4. Makefile --> which sets rules to manage the dependencies of the source files of the programs during the compilation and linking (build) phase.
5. Requirements.txt --> contains a list of packages/libraries needed to work on this project that can all be installed with the file.
6. main.py --> Reads a CSV file, generates descriptive summary statistics, and produces data visualizations.
7. test_main.py --> Tests the functionality of main.py by verifying the accuracy of the descriptive summary statistics and the correctness of the generated visualizations

## Functions inside the main.py
readData(df): Reads a CSV file into a DataFrame.
cleanData(df, Columns, Duplicate): Cleans the data by removing duplicates and selecting specified columns.
summaryStatistics(df): Generates descriptive summary statistics, including median, for numeric columns in the DataFrame.
stackPlot(df, xVal, StackVal): Creates a stacked bar plot based on two categorical variables.
barPlot(df, xVal, yVal, Segregate): Produces a horizontal bar plot showing the average of one variable grouped by two others.
