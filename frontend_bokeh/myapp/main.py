import random

from bokeh.driving import count
from bokeh.io import curdoc
from bokeh.models.widgets import (Div)

#function for streaming
def get_price(t):
    value = 10.7 + t / 100 - (t / 100 ) ** 0.5 - random.uniform(0.001,0.05)
    return round(value*100)/100

stock_name = '0'
price = '10.7'
percentage = "20"
#template for the text and numbers that appear
template=("""
      <div class='content'>
       <div id='getrandnum'> {stock_name} </div>
      </div>
      """)
# initial text
text = template.format(stock_name = stock_name,)
div = Div(text=text, height=300)


    
curdoc().add_root(div)