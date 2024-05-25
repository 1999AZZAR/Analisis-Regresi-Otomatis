# Tutorial: Analisis Regresi Linear Berganda Menggunakan Python

Tutorial ini menunjukkan cara membuat program Python untuk melakukan uji parsial (uji t), uji simultan (uji F), dan menghitung koefisien determinasi dalam analisis regresi linear berganda. Program ini juga menghasilkan laporan dalam format Excel dan menampilkan bagan regresi.

## Langkah-langkah

### 1. Persiapkan Lingkungan Python

Pastikan Anda sudah menginstal library yang dibutuhkan. Anda dapat menginstal semuanya menggunakan pip:

```bash
pip install pandas statsmodels matplotlib openpyxl
```

### 2. Siapkan Data (*pilih salah satu baik csv maupun xlsx)

#### Contoh Format CSV

Simpan data ini sebagai `data.csv`:

```csv
Y,X1,X2,X3
10,1,5,8
15,2,3,6
20,3,6,7
25,4,8,10
30,5,10,12
35,6,12,14
40,7,14,16
45,8,16,19
50,9,18,21
55,10,20,23
60,11,22,25
65,12,24,28
70,13,26,30
75,14,28,33
80,15,30,35
85,16,32,37
90,17,34,39
95,18,36,42
100,19,38,44
105,20,40,46
```

#### Contoh Format XLSX

Simpan data ini sebagai `data.xlsx`. Anda bisa membuatnya menggunakan Excel atau dengan Pandas:

##### Menggunakan Excel

1. Buka Microsoft Excel.
2. Masukkan data ke dalam sel seperti berikut:

|  Y  |  X1  |  X2  |  X3  |
|-----|------|------|------|
|  10 |  1   |  5   |  8   |
|  15 |  2   |  3   |  6   |
|  20 |  3   |  6   |  7   |
|  25 |  4   |  8   |  10  |
|  30 |  5   |  10  |  12  |
|  35 |  6   |  12  |  14  |
|  40 |  7   |  14  |  16  |
|  45 |  8   |  16  |  19  |
|  50 |  9   |  18  |  21  |
|  55 |  10  |  20  |  23  |
|  60 |  11  |  22  |  25  |
|  65 |  12  |  24  |  28  |
|  70 |  13  |  26  |  30  |
|  75 |  14  |  28  |  33  |
|  80 |  15  |  30  |  35  |
|  85 |  16  |  32  |  37  |
|  90 |  17  |  34  |  39  |
|  95 |  18  |  36  |  42  |
| 100 |  19  |  38  |  44  |
| 105 |  20  |  40  |  46  |

3. Simpan file dengan nama `data.xlsx`.

##### Menggunakan Pandas

Berikut adalah cara membuat file XLSX menggunakan Pandas:

```python
import pandas as pd

data = {
    'Y': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    'X1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'X2': [5, 3, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    'X3': [8, 6, 7, 10, 12, 14, 16, 19, 21, 23, 25, 28, 30, 33, 35, 37, 39, 42, 44, 46]
}

df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)
```

### 3. Buat Program Python

Buat program Python berikut dan simpan sebagai `regression_analysis.py`:

```python
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Fungsi untuk membaca data
def read_data(file_path):
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("File harus berformat .csv atau .xlsx")
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
def main(file_path, dependent_var, independent_vars, report_file_path):
    data = read_data(file_path)
    model = multiple_regression(data, dependent_var, independent_vars)
    create_report(model, report_file_path)
    create_plot(data, dependent_var, independent_vars, model)

    print("Uji t, Uji F, dan Koefisien Determinasi")
    print(model.summary())

if __name__ == "__main__":
    # Ganti dengan file path Anda
    file_path = 'data.xlsx'
    dependent_var = 'Y'  # Ganti dengan nama variabel dependen Anda
    independent_vars = ['X1', 'X2', 'X3']  # Ganti dengan nama variabel independen Anda
    report_file_path = 'regression_report.xlsx'

    main(file_path, dependent_var, independent_vars, report_file_path)
```

### 4. Jalankan Program

Pastikan Anda berada dalam direktori yang sama dengan `regression_analysis.py` dan file data (`data.csv` atau `data.xlsx`), kemudian jalankan program:

```bash
python regression_analysis.py
```

### 5. Hasil

Program akan membaca data dari file, melakukan analisis regresi berganda, menghasilkan laporan dalam format Excel (`regression_report.xlsx`), dan menampilkan bagan regresi.

### Struktur Direktori

Pastikan struktur direktori Anda seperti ini:

```
regression_analysis/
│
├── data.csv
├── data.xlsx
├── regression_analysis.py
├── regression_report.xlsx (akan dibuat setelah menjalankan program)
```

Dengan mengikuti langkah-langkah ini, Anda akan dapat melakukan analisis regresi berganda secara otomatis dan mendapatkan laporan yang sesuai dengan SPSS dalam format Excel.

### 6. Contoh Hasil Program

Setelah menjalankan program, Anda akan melihat output di terminal dan file Excel yang dihasilkan. Berikut adalah contoh hasil:

#### Output di Terminal

Output yang dihasilkan di terminal akan memberikan detail statistik dari regresi berganda, termasuk uji parsial (uji t) dan uji simultan (uji F):

```
Uji t, Uji F, dan Koefisien Determinasi
                            OLS Regression Results
==============================================================================
Dep. Variable:                      Y   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                  1.000
Method:                 Least Squares   F-statistic:                 1.764e+29
Date:                Sat, 25 May 2024   Prob (F-statistic):          2.33e-228
Time:                        23:27:38   Log-Likelihood:                 561.08
No. Observations:                  20   AIC:                            -1114.
Df Residuals:                      16   BIC:                            -1110.
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          5.0000   1.11e-13   4.51e+13      0.000       5.000       5.000
X1             5.0000    1.2e-13   4.17e+13      0.000       5.000       5.000
X2         -3.553e-15   1.09e-13     -0.033      0.974   -2.34e-13    2.27e-13
X3         -3.553e-15   6.72e-14     -0.053      0.959   -1.46e-13    1.39e-13
==============================================================================
Omnibus:                        3.086   Durbin-Watson:                   0.009
Prob(Omnibus):                  0.214   Jarque-Bera (JB):                1.281
Skew:                           0.124   Prob(JB):                        0.527
Kurtosis:                       1.785   Cond. No.                         158.
==============================================================================
```

#### Laporan dalam Format Excel

File Excel `regression_report.xlsx` akan berisi laporan hasil regresi. Contoh isi laporan:

```csv
|           | Coef.      | Std.Err.  | t          |   P>|t|  |   [0.025   |   0.975]  |
|-----------|------------|-----------|------------|----------|------------|-----------|
|const      |    5.0000  | 1.11e-13  | 4.51e+13   |   0.000  |     5.000  |     5.000 |
|X1         |    5.0000  |  1.2e-13  | 4.17e+13   |   0.000  |     5.000  |     5.000 |
|X2         |-3.553e-15  | 1.09e-13  |   -0.033   |   0.974  | -2.34e-13  |  2.27e-13 |
|X3         |-3.553e-15  | 6.72e-14  |   -0.053   |   0.959  | -1.46e-13  |  1.39e-13 |
```

#### Bagan Regresi

Program akan menampilkan bagan regresi menggunakan matplotlib.

[![demo.png]](regression_plot.png)

Untuk menyimpan bagan sebagai gambar, Anda dapat menambahkan kode berikut dalam fungsi `create_plot`:

```python
plt.savefig('regression_plot.png')
```

Dengan mengikuti tutorial ini, Anda dapat menjalankan analisis regresi berganda secara otomatis dan mendapatkan hasil yang komprehensif.
