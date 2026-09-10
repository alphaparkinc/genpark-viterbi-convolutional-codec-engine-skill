class ConvolutionalViterbi:
    """
    Convolutional Encoder (Rate 1/2, K=3) and Viterbi Maximum-Likelihood Decoder.
    """
    def encode(self, bits):
        shift = [0, 0]
        out = []
        for b in bits:
            c0 = b ^ shift[0] ^ shift[1]
            c1 = b ^ shift[1]
            out.extend([c0, c1])
            shift = [b, shift[0]]
        return out

    def decode(self, received):
        steps = len(received) // 2
        path_costs = {0: 0}
        path_history = {0: []}

        for step in range(steps):
            r0 = received[2 * step]
            r1 = received[2 * step + 1]
            new_costs = {}
            new_history = {}

            for state, cost in path_costs.items():
                for b in (0, 1):
                    s0 = (state >> 1) & 1
                    s1 = state & 1
                    c0 = b ^ s0 ^ s1
                    c1 = b ^ s1
                    next_state = (b << 1) | s0
                    metric = (r0 ^ c0) + (r1 ^ c1)
                    total_cost = cost + metric
                    if next_state not in new_costs or total_cost < new_costs[next_state]:
                        new_costs[next_state] = total_cost
                        new_history[next_state] = path_history[state] + [b]

            path_costs = new_costs
            path_history = new_history

        best_state = min(path_costs, key=path_costs.get)
        return path_history[best_state]
