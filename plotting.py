from motion import df
from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool,ColumnDataSource

df["Entry_time"]=df["Entry"].dt.strftime("%d-%m-%Y %H:%M:%S")
df["Exit_time"]=df["Exit"].dt.strftime("%d-%m-%Y %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',width=500,height=100,title="Motion Graph",logo=None,responsive=True)
p.xaxis.axis_label="Time"
p.xaxis.axis_label_text_font_size="16pt"
p.title.text_font_size="20pt"
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1
hover=HoverTool(tooltips=[("Start","@Entry_time"),("End","@Exit_time")])
p.add_tools(hover)
p.quad(left="Entry",right="Exit",top=1,bottom=0,color="#abed76",source=cds)

output_file("Motion Graph.html")
show(p)