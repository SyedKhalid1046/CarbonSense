# 🌱 Carbon Sense — Carbon Emission Calculator

<p align="center">
  <img src="assets/carbon-sense-banner.png" alt="Carbon Sense - Carbon Emission Calculator" width="100%">
</p>

<h3 align="center">🌍 Understand Your Carbon Footprint. Make Greener Choices.</h3>

<p align="center">
  A Flask-based web application that estimates product-related CO₂ emissions and suggests simple environmental actions.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0.0-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/HTML-CSS-orange?logo=html5&logoColor=white" alt="HTML and CSS">
  <img src="https://img.shields.io/badge/Focus-Environment-2e8b57?logo=leaf&logoColor=white" alt="Environment">
</p>

---

## 📌 About the Project

**Carbon Sense** is a web application designed to make people more aware of the estimated carbon emissions associated with everyday products.

Users can upload a product image. The application checks the filename for a supported product name, looks up its configured CO₂ emission value, and provides a corresponding environmental suggestion.

## ✨ Key Features

- 📷 **Product Image Upload** — Upload supported product image formats.
- 🌍 **CO₂ Emission Estimation** — Retrieve an estimated emission value from the application's product dataset.
- 🌿 **Eco-Friendly Suggestions** — Receive suggestions such as recycling, tree planting, or carbon-offset programs.
- 🛡️ **File Validation** — Validate supported image formats and limit uploads to 5 MB.
- ⚡ **Simple Web Interface** — Interact with the application through a browser.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and calculations |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | User interface styling |
| Werkzeug | Secure filename handling and request utilities |

## ⚙️ How It Works

1. Open the Carbon Sense web application.
2. Upload a product image with a supported product name in its filename.
3. The application checks the filename against its configured product list.
4. The matching product's stored CO₂ value is displayed.
5. An environmental suggestion is generated based on the emission value.

> **Note:** The current version uses filename matching and predefined emission values. It does not automatically recognize products from image pixels. Emission figures are estimates and may differ from real-world product footprints.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/SyedKhalid1046/CarbonSense.git
```

### 2. Open the project folder

```bash
cd CarbonSense
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

Visit:

```text
http://127.0.0.1:5000
```

## 📸 Screenshots

Add screenshots of the actual application interface here.

| Application Interface | Emission Result |
|---|---|
| Add your home-page screenshot | Add your results-page screenshot |

To display screenshots, upload image files to the `assets/` folder and replace this section with their actual filenames.

## 🔮 Future Improvements

- 🤖 Add image-based product recognition.
- 📊 Expand the product emission dataset with reliable sources.
- 📈 Display emission comparisons and visual charts.
- 💾 Store calculation history for users.
- ☁️ Deploy the application online.

## 🎯 Project Objective

The goal of Carbon Sense is to make carbon-emission awareness more accessible and encourage people to consider the environmental impact of everyday products.

## 👨‍💻 Author

**Syed Khalid S K**

- GitHub: [@SyedKhalid1046](https://github.com/SyedKhalid1046)

---

<p align="center">
  🌱 <b>Small Actions. Greener Future.</b> 🌍
</p>
