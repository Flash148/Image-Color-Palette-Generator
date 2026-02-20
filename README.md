# 🎨 Image Color Palette Generator

A web-based tool that extracts dominant color palettes from uploaded images using K-Means clustering. Perfect for designers, developers, and creatives who need quick access to hex codes and RGB values for their projects.

## ✨ Features 

- **Smart Color Extraction** - Uses K-Means machine learning algorithm to identify dominant colors
- **Customizable Output** - Extract 2-10 colors based on your needs
- **One-Click Copy** - Click any hex code to instantly copy to clipboard
- **Visual Percentage Display** - See exactly how much of each color appears in your image
- **Responsive Design** - Works beautifully on desktop, tablet, and mobile
- **Clean Modern UI** - Professional interface with smooth animations

## 🛠️ Technologies Used

**Backend:**
- Python 3.13
- Flask 3.1.3
- Pillow (PIL) 12.0.0
- NumPy 2.4.2
- scikit-learn 1.8.0

**Frontend:**
- HTML5
- CSS3 (with CSS Grid and Flexbox)
- JavaScript (Clipboard API)

**Algorithm:**
- K-Means Clustering for color quantization

## 📥 Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/Flash148/Image-Color-Palette-Generator.git
   cd Image-Color-Palette-Generator
```

2. **Create a virtual environment:**
```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Run the application:**
```bash
   python app.py
```

5. **Open in browser:**
   Navigate to `http://localhost:5000`

## 🚀 Usage

1. Click "Choose an image" and select a JPG, PNG, or other image file
2. Select how many colors you want to extract (2-10)
3. Click "Extract Colors ✨"
4. View your color palette with hex codes, RGB values, and percentages
5. Click any hex code to copy it to your clipboard

## 🔮 Future Improvements

- [ ] **Batch Processing** - Upload and analyze multiple images at once
- [ ] **Website Color Extraction** - Extract color palettes from live websites by URL
- [ ] **Export Options** - Download palettes as PNG swatches or CSS variables
- [ ] **Color Naming** - Add human-readable color names (e.g., "Coral Red", "Ocean Blue")
- [ ] **Palette Suggestions** - Generate complementary and analogous color schemes
- [ ] **Color History** - Save and compare palettes from different images
- [ ] **API Endpoint** - Allow programmatic access for developers

## 📸 Screenshots

![Upload Interface](screenshots/upload.png)
![Color Palette Results](screenshots/results.png)

*Note: Screenshots coming soon*

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Mike Robbins**
- GitHub: [@Flash148](https://github.com/Flash148)
- Portfolio: [mikerobbins.vercel.app](https://mikerobbins.vercel.app/)

---

⭐ If you found this project helpful, please consider giving it a star!