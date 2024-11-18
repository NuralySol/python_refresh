# 🐍 Python Refresh: Basics of Python, Pandas, Matplotlib, and Data Scraping

---

## 📊 **1. Pandas**

**Pandas** is a powerful Python library for data manipulation and analysis, providing structures like **DataFrame** and **Series** for handling structured data.

### ✨ **Key Features:**

- **🔄 Data Wrangling:** Clean and prepare data for analysis.
- **📂 File I/O:** Read and write CSV, Excel, JSON, SQL, and more.
- **📊 Data Analysis:** Perform aggregations, filtering, grouping, and joins.
- **📅 Time-Series Support:** Efficiently handle datetime objects.

### 🛠️ **Common Functions:**

- `read_csv()`, `to_csv()` → Read and write data files.
- `head()`, `tail()` → View top or bottom rows of the dataset.
- `describe()` → Get basic statistics about your data.
- `groupby()` → Perform group-based operations.
- `merge()`, `join()` → Combine datasets effectively.

---

## 📉 **2. Matplotlib**

**Matplotlib** is a Python library for creating static, interactive, and animated visualizations.

### ✨ **Key Features:**

- Supports diverse chart types: 📈 Line, 📊 Bar, ⚪ Scatter, 🟠 Pie, 📉 Histogram, and more.
- Highly customizable with titles, labels, legends, colors, and markers.
- Interactive visualizations using `plt.show()`.

### 🖍️ **Basic Workflow:**

1. **📥 Import the library:** `import matplotlib.pyplot as plt`.
2. **📊 Create a plot:** Use functions like `plt.plot()`, `plt.bar()`, `plt.scatter()`, etc.
3. **⚙️ Customize:** Add titles, labels, and legends.
4. **📤 Display or Save:** Use `plt.show()` to display or `plt.savefig()` to save the plot.

---

## 🌐 **3. Data Scraping**

Data scraping is the process of extracting structured information from websites or online sources. It involves fetching HTML content and parsing it to extract meaningful data.

### 🔍 **What is Data Scraping?**

- Extracts data such as **text**, **images**, **tables**, or **links** from web pages.
- Used for building datasets, gathering insights, or automation.

### 📚 **Common Libraries for Data Scraping in Python:**

- **🌐 `requests`:** Fetch raw HTML content from web pages.
- **🧼 `BeautifulSoup` (bs4):** Parse and extract data from HTML or XML.
- **⚙️ `selenium`:** Automate browsers to handle dynamic content.
- **🕷️ `Scrapy`:** Framework for large-scale scraping projects.

### 🛠️ **Basic Steps for Data Scraping:**

#### **Step 1: Send a Request**

- Fetch the web page's HTML content using `requests.get(URL)`.
- Example:

  ```python
  import requests
  response = requests.get("https://example.com")
  html = response.text
