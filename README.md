# Passport Photo Maker
A python program for generating passport photos that comply with [ICA's photo guidelines](https://www.ica.gov.sg/photo-guidelines).

# Requirements
1. Photo must show a face, neck and shoulders, taken with a solid colored background (White preferred).
2. User provides a portrait photo with a minimum size of 400px (W) x 514px (H).
3. Program must downsize or crop the photo to the desired size of 400px (W) x 514px (H).
4. Program must remove all shadows from the background.
5. Program should try to smoothen or remove facial imperfections in the most natural way possible (Bonus). 


# Usage


```python
pip3 -r requirements.txt
python3 app.py
```