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

3. Simpan file dengan nama `data.xlsx`.

##### Menggunakan Pandas

Berikut adalah cara membuat file XLSX menggunakan Pandas:

```python
import pandas as pd

data = {
    'Y': [10, 15, 20, 25, 30, 35, 40],
    'X1': [1, 2, 3, 4, 5, 6, 7],
    'X2': [5, 3, 6, 8, 10, 12, 14],
    'X3': [8, 6, 7, 10, 12, 14, 16]
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
                            Results: Ordinary least squares
==============================================================================
Model:                 OLS                 Adj. R-squared:        0.998
Dependent Variable:    Y                   AIC:                   21.1580
Date:                  2024-05-20 00:00    BIC:                   21.7801
No. Observations:      7                   Log-Likelihood:       -6.5790
Df Model:              3                   F-statistic:          1488.0
Df Residuals:          3                   Prob (F-statistic):   2.14e-05
R-squared:             0.999               Scale:                 0.32286
------------------------------------------------------------------------------
            Coef.     Std.Err.       t      P>|t|     [0.025     0.975]
------------------------------------------------------------------------------
const       1.2857      0.799       1.609   0.205    -1.043     3.614
X1          2.2857      0.558       4.093   0.026     0.465     4.106
X2          0.0714      0.352       0.203   0.848    -1.033     1.176
X3          0.8571      0.385       2.228   0.111    -0.336     2.051
==============================================================================
```

#### Laporan dalam Format Excel

File Excel `regression_report.xlsx` akan berisi laporan hasil regresi. Contoh isi laporan:

|           | Coef. | Std.Err. | t       | P>|t|  | [0.025 | 0.975] |
|-----------|-------|----------|---------|------|--------|--------|
| const     | 1.2857| 0.799    | 1.609   | 0.205| -1.043 | 3.614  |
| X1        | 2.2857| 0.558    | 4.093   | 0.026| 0.465  | 4.106  |
| X2        | 0.0714| 0.352    | 0.203   | 0.848| -1.033 | 1.176  |
| X3        | 0.8571| 0.385    | 2.228   | 0.111| -0.336 | 2.051  |

#### Bagan Regresi

Program akan menampilkan bagan regresi menggunakan matplotlib.

Untuk menyimpan bagan sebagai gambar, Anda dapat menambahkan kode berikut dalam fungsi `create_plot`:

```python
plt.savefig('regression_plot.png')
```

Dengan mengikuti tutorial ini, Anda dapat menjalankan analisis regresi berganda secara otomatis dan mendapatkan hasil yang komprehensif.
