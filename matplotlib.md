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

## using html hex string
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

# Lines and markers
- alpha = 0.7
- antialiased = True
- ls (linestyle)
![line styles](https://github.com/freemao/matplotlib/blob/master/linestyles.png)
- lw (linewidth)
- marker
![markers](https://github.com/freemao/matplotlib/blob/master/markers.png)
- mew (markeredgewidth)
- mec (markeredgecolor)
- mfc (markerfacecolor)
- ms (markersize)

# scatter
specify different colors and size for your dots  
`colors = np.random.rand(N)`  
`area = np.pi * (15 * np.random.rand(N))**2` # 0 to 15 point radii  
`plt.scatter(x, y, s=area, c=colors, alpha=0.5)`  
![scatter_examplt](https://github.com/freemao/matplotlib/blob/master/scatter.png)  

# Coordinate setting
`ax.set_xlim([0,1])`  
`ax.set_xlim(left=0)`  #only specify left boundary  
`ax.set_xlim(right=1)` #only specify left boundary  

`ax.set_ylim([0,1])`  
`ax.set_ylim(bottom=0)`  
`ax.set_ylim(top=1)`  

`ax.set_xticks()`  
`ax.set_xticks([])` #give an empty list to show without ticks  
`ax.set_xticklabels()`  

`ax.set_yticks()`  
`ylabel = ['%.2f'%i for i in np.arange(0,0.61, 0.1)]`  
`ylabel[0] = ''`  
`ax.set_yticklabels(ylabel)`  

# Ticks
Learning
<http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html#tick-locators>

# Continue...
