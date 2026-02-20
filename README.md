# Image Color Palette Generator

A web-based tool that extracts dominant color palettes from uploaded images using K-Means clustering. Perfect for designers, developers, and creatives who need quick access to hex codes and RGB values for their projects.

## ✨ Features 

- Smart Color Extraction - Uses K-Means machine learning algorithm to identify dominant colors
- Customizable Output - Extract 2-10 colors based on your needs
- Click Copy - Click any hex code to instantly copy to clipboard
- Visual Percentage Display - See exactly how much of each color appears in the image
- Responsive Design - Works beautifully on desktop, tablet, and mobile
- Clean Modern UI - Interface with smooth animations


## ⚙️ Tech Stack
Backend
- Python 3.13
- Flask 3.1.3
- Pillow (PIL) 12.0.0
- NumPy 2.4.2
- scikit-learn 1.8.0

Frontend
- HTML5
- CSS3 (with CSS Grid and Flexbox)
- JavaScript (clipboard api)

Algorithm
- K-Means Clustering for color quantization

## Intallation
1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Image-Color-Palette-Generator.git
cd Image-Color-Palette-Generator
```

2. Create a virtual environment
```bash
python -m venv venv

#on windows:
venv\Scripts\activate

#on Mac/Linux:
source venv/bin/activate

3. Install dependencies
```bash
pip install -r requirements.txt
```

4.