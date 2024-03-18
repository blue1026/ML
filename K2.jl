using CSV
using DataFrames
using Clustering
using Random
using Distances
using Plots

N_CLUSTERS = 3
Random.seed!(0)

function get_average_distance(kmeans_result::KmeansResult, df::DataFrame)::Float64
    total = 0
    [total+=euclidean(convert(Vector{Float64}, collect(df[i, :])), kmeans_result.centers[:, kmeans_result.assignments[i]]) for i in 1:nrow(df)]
    return total /= nrow(df)
end

df = CSV.read("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\dye.csv", DataFrame)
df = df[:, Not([:"class"])]

R = kmeans(Matrix(df)', N_CLUSTERS)
num_iterations = R.iterations

CSV.write("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\cluster3.csv", DataFrame(R.centers', ["d1"; "c1"; "d2"; "c2"; "d3"; "c3"]))

avg_dist_vs_iters = [get_average_distance(R, df) for R in [kmeans(Matrix(df)', N_CLUSTERS, maxiter=i) for i in 1:num_iterations]]

averageDistanceVsIteration = plot(avg_dist_vs_iters)
kmeansCenter = scatter(R.centers[1, :], R.centers[2, :])

plot(kmeansCenter, averageDistanceVsIteration, 
     layout=grid(1, 2), 
     legend=false, 
     xlabel=["d1" "number of iteration"], 
     ylabel=["c1" ""], 
     title=["kmeans center" ""]
)