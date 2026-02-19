"""
Carbon Sense - Carbon Emission Calculator
A Flask application that calculates CO2 emissions from products 
and suggests natural offset solutions.
"""

from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ==================== Configuration ====================
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==================== Data ====================
# Product CO2 Emission Values (kg equivalent)
product_co2 = {
    "cotton t-shirt": 2.1,
    "jeans": 33,
    "polyester shirt": 5.5,
    "shoes": 14,
    "smartphone": 55,
    "laptop": 200,
    "smart watch": 20,
    "television": 300,
    "plastic bottle": 0.08,
    "shampoo bottle": 0.5,
    "plastic cover": 0.02,
    "toothbrush": 0.03,
    "beef": 27,
    "chicken": 6.9,
    "rice": 4,
    "vegetables": 2,
    "petrol": 2.3,
    "diesel": 2.7,
    "car": 7000,
    "bike": 1200
}

# ==================== Utility Functions ====================

def allowed_file(filename):
    """Check if uploaded file has allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_solution(co2):
    """
    Get natural offset solution based on CO2 emission value.
    
    Args:
        co2 (float): CO2 emission in kilograms
        
    Returns:
        str: Recommended natural offset solution
    """
    if co2 < 1:
        return "Avoid plastic / recycle"
    elif co2 < 5:
        return "Plant 1 tree"
    elif co2 < 20:
        return "Plant 5 trees"
    elif co2 < 100:
        return "Solar usage + tree plantation"
    else:
        return "Carbon offset program"

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route for calculating carbon emissions.
    Handles GET (display form) and POST (process upload and calculate).
    """
    result = None
    solution = None
    product_found = None
    error = None

    if request.method == "POST":
        # Validate file existence
        if "image" not in request.files:
            error = "No file uploaded. Please select an image."
        else:
            image = request.files["image"]
            
            # Validate file selection
            if image.filename == "":
                error = "No file selected. Please choose an image."
            # Validate file extension
            elif not allowed_file(image.filename):
                error = "Invalid file type. Please upload: PNG, JPG, JPEG, GIF, or WebP."
            else:
                try:
                    # Get secure filename and save file
                    filename = secure_filename(image.filename).lower()
                    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                    image.save(filepath)

                    # Detect product from filename
                    product_detected = False
                    for product in product_co2:
                        if product in filename:
                            co2 = product_co2[product]
                            product_found = product.title()
                            result = f"{co2} kg CO₂"
                            solution = get_solution(co2)
                            product_detected = True
                            break

                    # Handle unrecognized product
                    if not product_detected:
                        result = "Product not recognized"
                        solution = "Please upload an image with a product name in the filename (e.g., 'shirt.jpg' or 'laptop.png')"
                        error = None
                        
                except Exception as e:
                    error = f"Error processing file: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        solution=solution,
        product_found=product_found,
        error=error
    )

# ==================== Error Handlers ====================

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error."""
    return render_template(
        "index.html",
        error="File too large. Maximum size is 5MB."
    ), 413

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template("index.html", error="Page not found."), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 server errors."""
    return render_template("index.html", error="Server error occurred."), 500

# ==================== Main ====================

if __name__ == "__main__":
    app.run(debug=True)
