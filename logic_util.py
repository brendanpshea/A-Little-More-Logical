def validate_probabilities(*probs):
  """Validates that each probability value is between 0 and 1."""
  if any(not 0 <= p <= 1 for p in probs):
    raise ValueError("Probabilities must be between 0 and 1.")

def complement_rule(pr_e):
    """Calculates the probability that event E doesn't occur."""
    validate_probabilities(pr_e)
    complement = 1 - pr_e
    print(f"P(not E) = 1 - P(E)")
    print(f"         = 1 - {pr_e}")
    print(f"         = {complement}")

def conditional_probability(pr_a, pr_b, pr_a_and_b):
    """Calcutates the probability of A, given that B is true"""
    validate_probabilities(pr_a, pr_b, pr_a_and_b)
    if pr_b == 0:
        raise ValueError("P(B) cannot be 0.")
    pr_a_given_b = pr_a_and_b / pr_b
    return f"P(A|B) = P(A and B) / P(B) = {pr_a_and_b} / {pr_b} = {pr_a_given_b}"

def simple_addition(pr_e1, pr_e2):
    """Calculates the probability either E1 or E2 occur."""
    validate_probabilities(pr_e1, pr_e2)
    result = pr_e1 + pr_e2
    print(f"P(E1 or E2) = P(E1) + P(E2)")
    print(f"            = {pr_e1} + {pr_e2}")
    print(f"            = {result}")


def general_addition(pr_e1, pr_e2, pr_e1_and_e2 = 0):
    """Calculates the probability either E1 or E2 occur."""
    validate_probabilities(pr_e1, pr_e2, pr_e1_and_e2)
    result = pr_e1 + pr_e2 - pr_e1_and_e2
    print(f"P(E1 or E2) = P(E1) + P(E2) - P(E1 and E2)")
    print(f"            = {pr_e1} + {pr_e2} - {pr_e1_and_e2}")
    print(f"            = {result}")

def simple_multiplication(pr_e1, pr_e2):
    """Calculates the probability both E1 and E2 occur (assumes independence)."""
    validate_probabilities(pr_e1, pr_e2)
    result = pr_e1 * pr_e2
    print(f"P(E1 and E2) = P(E1) * P(E2)")
    print(f"             = {pr_e1} * {pr_e2}")
    print(f"             = {result}")

def complete_multiplication(pr_e1_given_e2, pr_e2):
    """Calculates the probability bott E1 and E2 occur (may not be indpendent)."""
    validate_probabilities(pr_e2, pr_e1_given_e2)
    result = pr_e1_given_e2 * pr_e2
    print(f"P(E1 and E2) = P(E1|E2) * P(E2)")
    print(f"             = {pr_e1_given_e2} * {pr_e2}")
    print(f"             = {result}")

def total_probability(pr_e_given_h1, pr_h1, pr_e_given_h2, pr_h2):
    """
    Calculates the total probability of an event E given two exclusive hypotheses H1 and H2.
    """
    validate_probabilities(pr_e_given_h1, pr_h1, pr_e_given_h2, pr_h2)
    pr_e = pr_e_given_h1 * pr_h1 + pr_e_given_h2 * pr_h2
    return (f"P(E) = P(E|H1) * P(H1) + P(E|H2) * P(H2)\n"
            f"     = {pr_e_given_h1} * {pr_h1} + {pr_e_given_h2} * {pr_h2}\n"
            f"     = {pr_e}")
def bayes_theorem(p_h, pr_e_given_h, pr_e_given_not_h):
    """Calculates probability of a hypotheses being true, given some evidence."""
    validate_probabilities(p_h, pr_e_given_h, pr_e_given_not_h)
    p_not_h = 1 - p_h
    pr_e = pr_e_given_h * p_h + pr_e_given_not_h * p_not_h
    p_h_given_e = (pr_e_given_h * p_h) / pr_e
    print(f"P(H|E) = (P(E|H) * P(H)) / [P(E|H) * P(H) + P(E|not H) * P(not H)]")
    print(f"       = ({pr_e_given_h} * {p_h}) / ({pr_e_given_h} * {p_h} + {pr_e_given_not_h} * {p_not_h})")
    print(f"       = {round(p_h_given_e,2)}")