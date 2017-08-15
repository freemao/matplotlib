# Colors
## input colors name directly
- blue
- green
- red
- cyan
- magenta
- yellow
- back
- white

## gray 
- '0.95' 
- '0.75'
- '0.55' 
From 0 (darker) to 1 (lighter)

## using RBG tube (r,g,b)
- (0, 0, 0) black
- (1, 1, 1) white
- (0.5, 0.8, 0.5) greener
- (0.5, 0.5, 0.8) toward blue
- (0.8, 0.5, 0.5) toward red

## using an html hex string
- '#1b9e77'
- '#d95f02'
- '#7570b3'
- '#e7298a'

## colormaps
![colormaps](https://github.com/freemao/matplotlib/blob/master/colormaps.png)
append _r to use the reverse colormap. For exmaple:
cmap = plt.get_cmap('GnBu_r')

## recomended colors
you can use this website to choose [recommended colors](http://colorbrewer2.org/#type=qualitative&scheme=Accent&n=6)
![recommendedcolors](https://github.com/freemao/matplotlib/blob/master/recommendcolors.PNG)

# Text
<https://matplotlib.org/users/index_text.html>
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
<https://matplotlib.org/users/annotations.html>
- text s
- xy: coordinate for annotation
- xytext: coordinate for text
- arrowprops: define arrow between text pos and annotation pos.

## mathematical expression using Tex markup
<http://matplotlib.org/users/mathtext.html>  
Put expression in r'$...$'
- \lambda, \pi, \rho, \sigma, \theta, \Delta, \Pi, \sum, \lg, \ln, \log
- subscripts(^) and superscripts(_)
- fraction
- fontstyle


Freemao
cmiao@huskers.unl.edu
8/15/17
