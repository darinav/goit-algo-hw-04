import turtle
import argparse

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.tracer(False)

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.update()
    window.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Сніжинка Коха")
    parser.add_argument('recursion_depth', type=int, help='Глибина рекурсії')
    args = parser.parse_args()
    draw_koch_curve(args.recursion_depth)

if __name__ == "__main__":
    main()
