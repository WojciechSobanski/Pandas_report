import pandas as pd

data_1 = pd.read_excel("Data_1.xlsx")
data_2 = pd.read_excel("Data_2.xlsx")

report_1 = pd.concat([data_1, data_2], keys=['Data_1', 'Data_2'])

pivot = pd.pivot_table(report_1,
                       index="City", columns="Country",
                       values="Value", aggfunc="sum",
                       margins=True, margins_name="Total")
print(pivot)

pivot.plot()

pd.options.plotting.backend = "plotly"

pivot.plot.bar(barmode="group")