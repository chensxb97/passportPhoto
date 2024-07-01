# Passport Photo Maker
A python program for generating passport photos that comply with [ICA's photo guidelines](https://www.ica.gov.sg/photo-guidelines).

# Requirements
1. Photo must show a face, neck and shoulders.
3. Program will return an error if no face is detected.
3. Program must downsize or crop the photo to the desired size of 400px (W) x 514px (H).
4. Program must replace the existing background with a full solid white background.

# Usage

```python
pip -r requirements.txt
python app.py
```

# Acknowledgements
1. [removebg](https://github.com/danielgatis/rembg)
2. [Fireship's rembg-webapp-tutorial](https://github.com/codediodeio/rembg-webapp-tutorial)