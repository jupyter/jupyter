(tryjupyter)=

# Try Jupyter
import ipywidgets as widgets
from IPython.display import display

# 1. ውጤት ማሳያ ሳጥን (Screen) ማዘጋጀት
display_box = widgets.Text(
    value='',
    placeholder='0',
    description='',
    disabled=True,  # በተጠቃሚው በኪቦርድ እንዳይፃፍ ይከለክላል
    layout=widgets.Layout(width='265px', margin='5px')
)

# የሂሳብ ስሌቱን በፅሁፍ መልክ ይዞ የሚቆይ ተለዋዋጭ (Variable)
current_expression = ""

# 2. የአዝራር (Button) ክሊክ ተግባር መፍጠር
def on_button_click(b):
    global current_expression
    button_value = b.description  # የተጫነው አዝራር ስም
    
    if button_value == 'C':  # ማፅጃ
        current_expression = ""
        display_box.value = ""
    elif button_value == '=':  # ማጠቃለያ/ውጤት ማውጫ
        try:
            # eval የፅሁፍ ሂሳቡን በቀጥታ ወደ ስሌት ይቀይረዋል
            result = eval(current_expression)
            display_box.value = str(result)
            current_expression = str(result)
        except ZeroDivisionError:
            display_box.value = "ስህተት: ለ 0 ማካፈል አይቻልም!"
            current_expression = ""
        except Exception:
            display_box.value = "ስህተት"
            current_expression = ""
    else:
        current_expression += button_value
        display_box.value = current_expression

# 3. የአዝራሮች ስም ዝርዝር በረድፍ
button_labels = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# 4. አዝራሮችን ፈጥሮ በቅደም ተከተል ማደራጀት
grid_rows = []
for row in button_labels:
    row_buttons = []
    for label in row:
        # ለሂሳብ ምልክቶች ቢጫ ቀለም (warning) እንሰጣቸዋለን
        button_style = 'warning' if label in ['/', '*', '-', '+', '=', 'C'] else ''
        
        btn = widgets.Button(
            description=label,
            button_style=button_style,
            layout=widgets.Layout(width='60px', height='50px', margin='2px')
        )
        # አዝራሩ ሲጫን ከላይ የሰራነውን ተግባር እንዲጠራ ማድረግ
        btn.on_click(on_button_click)
        row_buttons.append(btn)
        
    # በጎን (Horizontal) ረድፎችን መፍጠር
    grid_rows.append(widgets.HBox(row_buttons))

# 5. ማሳያውንና ሁሉንም ረድፎች ወደላይ (Vertical) ማደራጀት
calculator_ui = widgets.VBox([display_box] + grid_rows)

# ካልኩሌተሩን በስክሪኑ ላይ ማሳየት
display(calculator_ui)
```{contents} Contents
:local:
```

These sections describe a few ways to get started with some of the most-commonly used tools in the Jupyter ecosystem.

## Try in Your Browser. No Installation Needed.


**Try Jupyter** (https://try.jupyter.org) is a site for trying out the Jupyter Notebook, equipped with kernels for several different languages (Julia, R, C++, Scheme, Ruby) without installing anything.
Click the link below t

o go to the page.

```{button-link} https://try.jupyter.org
:color: secondary
Click to Try Jupyter
```

When running the examples on the `Try Jupyter` site, you will get a temporary Jupyter
server running on mybinder.org which you can use to play around until you close your
browser session.

You can use this site to try a few of the major interactive computing interfaces created by the Jupyter community.
A description of each is below.

### Try the Classic Notebook interface

The *Classic Notebook* interface is a document-oriented interface that allows you to create, view, and execute code in a Jupyter Notebook.

The example should look like this:

**Notebook Dashboard**

```{image} ../_static/_images/tryjupyter_file.png
```

**Notebook Editor**

```{image} ../_static/_images/trynb.png
```

### Try the JupyterLab interface

The Jupyter Lab interface is a more extensible and composable interactive computing interface for more complex workflows.

Here's an example of what the JupyterLab interface looks like:

```{image} ../_static/_images/jupyterlab.png
```

## Next step: install Jupyter locally

If you have tried Jupyter and like it, please use our [Installation Guide](install) to install Jupyter on your computer.

```{toctree}
:maxdepth: 2

../install
../running
```
