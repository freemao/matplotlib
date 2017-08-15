# Text
## text(x, y, s, fontdict=None, withdash=False, **kwargs)
- x, y: the coordinate of your text
- s: content of your text
- dict. 
  - color=
  - alpha = 
  - fontsize=
  - fontstyle = 'normal', 'italic', 'oblique'
  - fontweight = [a numeric value in range 0-1000 | ‘ultralight’ | ‘light’ | ‘normal’ | ‘regular’ | ‘book’ | ‘medium’ | ‘roman’ | ‘semibold’ | ‘demibold’ | ‘demi’ | ‘bold’ | ‘heavy’ | ‘extra bold’ | ‘black’ ]
- bbox = dict(facecolor='red', alpha=0.5)
put a rectangular box around the text.

## set_xlabel(), set_ylabel()
- use same dict in text
- labelpad = 'define the distance between lable and axis'

## set_title()
- loc =  {‘center’, ‘left’, ‘right’}. default to 'center'

## annotate(s, xy=(x,y), xytext=(x,y), arrowprops=dict(arrowsytyle='->'))
- text s
- xy: coordinate for annotation
- xytext: coordinate for text
- arrowprops: define arrow between text pos and annotation pos.

## mathematical expression using Tex markup
<(http://matplotlib.org/users/mathtext.html)>
put expression in r'$...$'
- \lambda, \pi, \rho, \sigma, \theta, \Delta, \Pi, \sum, \lg, \ln, \log
- subscripts(^) and superscripts(_)
- fraction
- fontstyle


Freemao
cmiao@huskers.unl.edu
8/15/17
