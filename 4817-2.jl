abstract type AbstractPoint end

mutable struct MyPoint <: AbstractPoint
    x::Float64
    y::Float64
end

function Base.show(io::IO, p::MyPoint)
    println(io, "($(p.x), $(p.y))")
end

function distance_to(p1::MyPoint, p2::MyPoint)
    return sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)
end

mutable struct MyGroup <: AbstractPoint
    name::String
    pivot::MyPoint
    members::Vector{MyPoint}
    old_members::Vector{MyPoint}
end

function Base.show(io::IO, g::MyGroup)
    println(io, "【組別 $(g.name)】")
    println(io, "中心點: $(g.pivot)")
    println(io, "成員: ", join(g.members, ", "))
end

function no_member_update(g::MyGroup)::Bool
    return g.old_members == g.members
end

function update_pivot(g::MyGroup)
    if isempty(g.members)
        return
    end
    sum_x = sum(p.x for p in g.members)
    sum_y = sum(p.y for p in g.members)
    n = length(g.members)
    g.pivot.x = sum_x / n
    g.pivot.y = sum_y / n

    g.old_members = copy(g.members)
    empty!(g.members)
end

mutable struct MySample <: AbstractPoint
    point::MyPoint
    group::Union{MyGroup, Nothing}
end

function Base.show(io::IO, s::MySample)
    println(io, "$(s.point)")
end

function set_group!(s::MySample, groups::Vector{MyGroup})
    distances = [distance_to(s.point, group.pivot) for group in groups]
    min_dist_group = argmin(distances)
    s.group = groups[min_dist_group]
    push!(groups[min_dist_group].members, s.point)
end

# 主函數
function main()
    # 樣本點
    samples_data = [
        (2.0, 5.0), (3.0, 2.0), (3.0, 3.0), (3.0, 4.0), (4.0, 3.0),
        (4.0, 4.0), (6.0, 3.0), (6.0, 4.0), (6.0, 6.0), (7.0, 2.0),
        (7.0, 5.0), (7.0, 6.0), (7.0, 7.0), (8.0, 6.0), (8.0, 7.0)
    ]

    # 分組點
    group_data = [
        ("1", 2.0, 2.0), ("2", 4.0, 6.0),
        ("3", 6.0, 5.0), ("4", 8.0, 8.0)
    ]

    # 轉換樣本點
    samples = [MySample(MyPoint(x, y), nothing) for (x, y) in samples_data]

    # 轉換分組點
    groups = [MyGroup(string(id), MyPoint(x, y), [], []) for (id, x, y) in group_data]

    # 搜索並更新直到沒有成員更改
    iteration = 0
    while true
        iteration += 1
        println("\n第 $iteration 次迭代")

        # 搜索
        for sample in samples
            set_group!(sample, groups)
        end

        # 平均距離
        mean_distance = sum(distance_to(sample.point, sample.group.pivot) for sample in samples) / length(samples)
        println("\nK-means 平均距離: $mean_distance")

        # 檢查聚類是否完成
        if all(group -> no_member_update(group), groups)
            break
        end

        # 更新
        for group in groups
            update_pivot(group)
        end
    end
end

main()



