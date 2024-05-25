import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import os

# Fungsi untuk membaca data
def read_data(base_path):
    csv_path = base_path + '.csv'
    xlsx_path = base_path + '.xlsx'

    if os.path.exists(csv_path):
        data = pd.read_csv(csv_path)
    elif os.path.exists(xlsx_path):
        data = pd.read_excel(xlsx_path)
    else:
        raise ValueError("File tidak ditemukan dalam format .csv atau .xlsx")

    return data

# Fungsi untuk melakukan regresi berganda
def multiple_regression(data, dependent_var, independent_vars):
    X = data[independent_vars]
    y = data[dependent_var]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model

# Fungsi untuk membuat laporan hasil regresi
def create_report(model, file_path):
    report = Workbook()
    ws = report.active
    ws.title = "Regression Results"

    # Menulis summary regresi ke dalam file excel
    summary = model.summary2().tables[1]
    for r in dataframe_to_rows(summary, index=True, header=True):
        ws.append(r)

    # Menyimpan file
    report.save(file_path)

# Fungsi untuk membuat bagan
def create_plot(data, dependent_var, independent_vars, model):
    plt.figure(figsize=(10, 6))
    for var in independent_vars:
        plt.scatter(data[var], data[dependent_var], label=f'{var} vs {dependent_var}')
        plt.plot(data[var], model.predict(sm.add_constant(data[independent_vars])), color='red')
    plt.xlabel('Independent Variables')
    plt.ylabel(dependent_var)
    plt.legend()
    plt.title(f'Regression Plot of {dependent_var} vs Independent Variables')
    plt.show()

# Main function
def main(base_path, dependent_var, independent_vars, report_file_path):
    data = read_data(base_path)
    model = multiple_regression(data, dependent_var, independent_vars)
    create_report(model, report_file_path)
    create_plot(data, dependent_var, independent_vars, model)

    print("Uji t, Uji F, dan Koefisien Determinasi")
    print(model.summary())

if __name__ == "__main__":
    # Ganti dengan base path Anda (tanpa ekstensi)
    base_path = 'data'  # Data file without extension
    dependent_var = 'Y'  # Ganti dengan nama variabel dependen Anda
    independent_vars = ['X1', 'X2', 'X3']  # Ganti dengan nama variabel independen Anda
    report_file_path = 'regression_report.xlsx'

    main(base_path, dependent_var, independent_vars, report_file_path)
