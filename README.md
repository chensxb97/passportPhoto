# Passport Photo Maker
A python program for generating passport photos that comply with [ICA's photo guidelines](https://www.ica.gov.sg/photo-guidelines).

# Requirements
1. Photo must show a face, neck and shoulders, taken with a solid colored background (White preferred).
2. Program must downsize or crop the photo to the desired size of 400px (W) x 514px (H).
3. Program will return an error if no face is detected.

# Usage

```python
pip3 -r requirements.txt
python3 app.py
```