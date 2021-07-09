import turtle

t = turtle.Pen()

amt = 7
# amt = input()
# amt = int(amt)
s = 400

t.penup()        
t.forward(-950)
t.right(90)
t.forward(480)
t.left(90)
t.pendown()

def ltl1(size):
    t.forward(size)
    t.left(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.left(60)
    t.forward(size)

if amt > 2:
    for x in range(2, amt):
        exec(f'''def ltl{x}(size):  # Generating functions
            ltl{x-1}(size/3)
            t.left(60)
            ltl{x-1}(size/3)
            t.right(120)
            ltl{x-1}(size/3)
            t.left(60)
            ltl{x-1}(size/3)
        ''')
    exec(f"ltl{amt-1}(s)")