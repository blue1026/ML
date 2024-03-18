using CSV
using DataFrames
using Clustering
using Random

df = CSV.read("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\dye.csv", DataFrame)

clusters = Dict{Any, Array}()
[clusters[cls] = Matrix{Real}(undef, 0, ncol(df)-1) for cls in unique(df.class)]

for row in eachrow(df)
    clusters[row.class] = [clusters[row.class]; collect(row)[1:ncol(df)-1]']
end

[clusters[cls] = convert(Matrix{Float64}, clusters[cls][randperm(size(clusters[cls], 1))[1:50], :]) for cls in keys(clusters)]

cls_centers = vcat([kmeans(cluster', 2).centers' for cluster in values(clusters)]...)

centers_df = DataFrame(cls_centers, ["d1", "c1", "d2", "c2", "d3", "c3"])
CSV.write("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\centers.csv", centers_df)
print(centers_df)
