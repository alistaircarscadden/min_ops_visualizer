class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.extend([x])

    def dequeue(self):
        if(self.empty()):
            return None
        else:
            x = self.queue[0]
            self.queue = self.queue[1:len(self.queue)]
            return x

    def empty(self):
        if(len(self.queue) == 0):
            return True
        return False

# Treated as immutable state node within our DFS tree
class State:
    def __init__(self, start, method, value, depth):
        self.start = start
        self.method = method
        self.value = value
        self.depth = depth

    def to_string(self):
        return "{},{},{},{}".format(self.start, self.value, self.method, len(self.method))

# Return the mutation (mutation) of state (state)
def next_state(state, mutation):
    if(mutation == "!"):
        return State(state.start,
                 state.method + "!",
                 state.value ^ 1,
                 state.depth + 1)

    if(mutation == "<"):
        return State(state.start,
                 state.method + "<",
                 (state.value << 1 | state.value >> 7) & (255),
                 state.depth + 1)

    if(mutation == ">"):
        return State(state.start,
                 state.method + ">",
                 (state.value >> 1 | state.value << 7) & (255),
                 state.depth + 1)

# Add the children of state (s) to the queue (q)
def enqueue_children(q, s):
    q.enqueue(next_state(s, "!"))
    q.enqueue(next_state(s, "<"))
    q.enqueue(next_state(s, ">"))

# Find best solution from value (f) to value (t)
def first_best(f, t):
    # Create DFS Queue
    q = Queue()
    # Add initial state
    q.enqueue(State(f, "", f, 0))
    
    states_searched = 0
    optimal = [999] * 256

    # DFS search of all states
    while(not q.empty()):
        # Get the next state in the queue as "cur"
        cur = q.dequeue()
        states_searched += 1

        # If cur is the solution then we are done
        if(cur.value == t):
            break

        # If the value of the current state has been reached
        # before, but at a shorter depth, then we discard this
        # state (end the branch)
        if(optimal[cur.value] <= cur.depth):
            continue

        # Save this as the "best-yet" depth in the optimal list
        optimal[cur.value] = cur.depth

        # Adds the three next states to the end of the queue
        enqueue_children(q, cur)

    # Return optimal solution and how many states were searched
    return (cur, states_searched)

def main():
	# Loop through every pair 2D 0-256 : 256^2
    for value_from in range(0, 256):
        # Write each section to a new file
        with open(str(value_from) + ".txt", "w") as file:
            for value_to in range(0, 256):
                file.write(first_best(value_from, value_to)[0].to_string() + "\n")

if(__name__ == "__main__"):
    main()
