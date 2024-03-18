class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def Euclidean_Distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Test:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.point = Point(x, y)
        self.value = []
        self.oldvalue = None
        
    def __str__(self) -> str:
        value_str = ", ".join(str(value) for value in self.value)
        return f"【Test {self.name}】\npoint: {self.point}\nvalue: {value_str}"
    
    def no_value_update(self) -> bool:
        if self.value == []:
            return True
        return self.value == self.oldvalue
    
    def update_point(self):
        if self.value:
            total_x = sum(value.x for value in self.value)
            total_y = sum(value.y for value in self.value)
            new_x = total_x / len(self.value)
            new_y = total_y / len(self.value)
            self.point = Point(new_x, new_y)
            self.oldvalue = list(self.value)
            self.value.clear()

class Sample(Point):
    def set_test(self, tests) -> None:
        distances = {test.name: self.Euclidean_Distance(test.point) for test in tests}
        min_test_name = min(distances, key=distances.get)
        min_test = next(test for test in tests if test.name == min_test_name)
        min_test.value.append(self)
        self.group = min_test  

    def distance_to_group_point(self):
        return self.Euclidean_Distance(self.group.point)

if __name__ == "__main__":    
    with open("C:/Users/bluew/OneDrive/桌面/HW1 1114817/sample points.csv", "r") as fin:
        samples_data = [line.strip().split(",") for line in fin]
        samples = [Sample(int(x), int(y)) for x, y in samples_data]
    
    with open("C:/Users/bluew/OneDrive/桌面/HW1 1114817/test points.csv", "r") as fin:
        tests_data = [line.strip().split(",") for line in fin]
        tests = [Test(name, int(x), int(y)) for name, x, y in tests_data]
        

        
    completed_iterations = 0
    max_iterations = 5
    mean_distances = []  
    for iteration in range(1, max_iterations + 1):
        print(f"\n{'Iteration ' + str(iteration)}")

        for sample in samples:
            sample.set_test(tests)

        print("\n\n".join(str(test) for test in tests))

        if all(test.no_value_update() for test in tests):
            break

        for test in tests:
            test.update_point()

       
        mean_distance = sum([sample.distance_to_group_point() for sample in samples]) / len(samples)
        mean_distances.append(mean_distance)
        print(f"\nMean distance after Iteration {iteration}: {mean_distance}")

    if completed_iterations == max_iterations:
        print("Clustering did not converge within the maximum number of iterations.")
    
    
    print("\nAll mean distances:", mean_distances)


import matplotlib.pyplot as plt


for sample in samples:
    plt.scatter(sample.x, sample.y, color='blue', marker='x', label='Sample')


for test in tests:
    plt.scatter(test.point.x, test.point.y, color='green', marker='*', s=200, label=f'Final Test {test.name} Center', zorder=2)


for test in tests:
    plt.scatter(test.point.x, test.point.y, color='red', marker='o', label=f'Initial Test {test.name}', zorder=3)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering')
plt.legend()
plt.grid(True)
plt.show()






fig, axs = plt.subplots(1, 3, figsize=(15, 5))


for sample in samples:
    axs[0].scatter(sample.x, sample.y, color='blue', marker='x', label='Sample')


for test in tests:
    axs[1].scatter(test.point.x, test.point.y, color='green', marker='*', s=200, label=f'Test {test.name} Center')


for test in tests:
    axs[2].scatter(test.point.x, test.point.y, color='red', marker='o', label=f'Test {test.name}')


axs[0].set_title('Sample Points')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')

axs[1].set_title('Final Test Centers')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')

axs[2].set_title('Initial Test Centers')
axs[2].set_xlabel('X')
axs[2].set_ylabel('Y')


axs[0].legend()
axs[1].legend()
axs[2].legend()


plt.tight_layout()
plt.show()

