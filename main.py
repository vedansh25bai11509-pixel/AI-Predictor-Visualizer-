import numpy as np
import matplotlib.pyplot as plt
import turtle
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 5, 4, 5, 7])
m, c = np.polyfit(x, y, 1)
y_pred = m * x + c
print(f"Model Learned: y = {m:.2f}x + {c:.2f}")
plt.scatter(x, y, label="Actual Data")
plt.plot(x, y_pred, label="AI Prediction Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("AI Learning Visualization")
plt.legend()
plt.show()
screen = turtle.Screen()
screen.title("AI Prediction Simulation")

t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-200, -200)
t.pendown()
t.forward(400)
t.backward(200)
t.left(90)
t.forward(400)
t.penup()
t.color("red")

for i in range(len(x)):
    px = -200 + x[i]*50
    py = -200 + y_pred[i]*50
    t.goto(px, py)
    t.dot(10)

turtle.done()

