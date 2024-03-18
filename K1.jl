using CSV
using DataFrames
using Plots, StatsPlots

df = CSV.read("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\dye.csv", DataFrame)

# barplot for nclass
val_count = Dict{UInt8, UInt16}()
[val_count[cls]=0 for cls in unique(df.class)]
[val_count[cls]+=1 for cls in df.class]
barPlot4nClass = bar(val_count)

# boxplot for c1, c2 and c3
x = repeat([1, 2, 3], nrow(df))
y = Matrix(df[:, [:"c1", :"c2", :"c3"]])'
y = vcat(y...)
boxPlot4c1c2c3 = boxplot(x, y)

# Histogram of dye$c1
histogramOfDyeC1 = histogram(df.c1)

# boxplot c3 for each class
x = df.class
y = df.c3
boxPlotC3ForEachClass = boxplot(x, y)

plot(barPlot4nClass, boxPlot4c1c2c3, histogramOfDyeC1, boxPlotC3ForEachClass, 
     layout=grid(2, 2), 
     legend=false, 
     xlabel=["" "" "dye\$c1" ""], 
     ylabel=["" "" "Frequency" ""], 
     title=["barplot for nclass" "boxplot for c1, c2 and c3" "Histogram of dye\$c1" "boxplot c3 for each class"]
)