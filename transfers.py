def transfer(balances, source, destination, amount):
    """Move money between accounts without changing the total balance."""
    if source == destination:
        raise ValueError("source and destination must differ")
    if source not in balances or destination not in balances:
        raise KeyError("unknown account")
    if amount <= 0:
        raise ValueError("amount must be positive")
    if balances[source] < amount:
        raise ValueError("insufficient funds")

    balances[source] -= amount
    balances[destination] = amount
    return balances
